# This file is part of the Printrun suite.
#
# Printrun is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Printrun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Printrun.  If not, see <http://www.gnu.org/licenses/>.

import logging

try:
    import wx
except:
    logging.error(_("WX is not installed. This program requires WX to run."))
    raise

from printrun.utils import install_locale

install_locale('pronterface')

from .controls import ControlsSizer, add_extra_controls
from .viz import VizPane
from .log import LogPane
from .toolbar import MainToolbar

import wx.lib.agw.floatspin as floatspin

class ToggleablePane(wx.BoxSizer):
    def __init__(self, root, label, parentpanel, parentsizers):
        super(ToggleablePane, self).__init__(wx.HORIZONTAL)
        if not parentpanel: parentpanel = root.panel
        self.root = root
        self.visible = True
        self.parentpanel = parentpanel
        self.parentsizers = parentsizers
        self.panepanel = root.newPanel(parentpanel)
        self.button = wx.Button(parentpanel, -1, label, size=(22, 18), style=wx.BU_EXACTFIT)
        self.button.Bind(wx.EVT_BUTTON, self.toggle)

    def toggle(self, event):
        if self.visible:
            self.Hide(self.panepanel)
            self.on_hide()
        else:
            self.Show(self.panepanel)
            self.on_show()
        self.visible = not self.visible
        self.button.SetLabel(">" if self.button.GetLabel() == "<" else "<")


class LeftPaneToggleable(ToggleablePane):
    def __init__(self, root, parentpanel, parentsizers):
        super(LeftPaneToggleable, self).__init__(root, "<", parentpanel, parentsizers)
        self.Add(self.panepanel, 0, wx.EXPAND)
        self.Add(self.button, 0)

    def set_sizer(self, sizer):
        self.panepanel.SetSizer(sizer)

    def on_show(self):
        for sizer in self.parentsizers:
            sizer.Layout()

    def on_hide(self):
        for sizer in self.parentsizers:
            # Expand right splitterwindow
            if isinstance(sizer, wx.SplitterWindow):
                if sizer.shrinked:
                    button_width = self.button.GetSize()[0]
                    sizer.SetSashPosition(sizer.GetSize()[0] - button_width)
            else:
                sizer.Layout()


class LogPaneToggleable(ToggleablePane):
    def __init__(self, root, parentpanel, parentsizers):
        super(LogPaneToggleable, self).__init__(root, ">", parentpanel, parentsizers)
        self.Add(self.button, 0)
        pane = LogPane(root, self.panepanel)
        self.panepanel.SetSizer(pane)
        self.Add(self.panepanel, 1, wx.EXPAND)
        self.splitter = self.parentpanel.GetParent()

    def on_show(self):
        self.splitter.shrinked = False
        self.splitter.SetSashPosition(self.splitter.GetSize()[0] - self.orig_width)
        self.splitter.SetMinimumPaneSize(self.orig_min_size)
        self.splitter.SetSashGravity(self.orig_gravity)
        if hasattr(self.splitter, "SetSashSize"): self.splitter.SetSashSize(self.orig_sash_size)
        if hasattr(self.splitter, "SetSashInvisible"): self.splitter.SetSashInvisible(False)
        for sizer in self.parentsizers:
            sizer.Layout()

    def on_hide(self):
        self.splitter.shrinked = True
        self.orig_width = self.splitter.GetSize()[0] - self.splitter.GetSashPosition()
        button_width = self.button.GetSize()[0]
        self.orig_min_size = self.splitter.GetMinimumPaneSize()
        self.orig_gravity = self.splitter.GetSashGravity()
        self.splitter.SetMinimumPaneSize(button_width)
        self.splitter.SetSashGravity(1)
        self.splitter.SetSashPosition(self.splitter.GetSize()[0] - button_width)
        if hasattr(self.splitter, "SetSashSize"):
            self.orig_sash_size = self.splitter.GetSashSize()
            self.splitter.SetSashSize(0)
        if hasattr(self.splitter, "SetSashInvisible"): self.splitter.SetSashInvisible(True)
        for sizer in self.parentsizers:
            sizer.Layout()


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # this list will contain all controls that should be only enabled
        # when we're connected to a printer
        self.panel = wx.Panel(self, -1)
        self.reset_ui()
        self.statefulControls = []

    def reset_ui(self):
        self.panels = []
        self.printerControls = []

    def newPanel(self, parent, add_to_list=True):
        panel = wx.Panel(parent)
        self.registerPanel(panel, add_to_list)
        return panel

    def registerPanel(self, panel, add_to_list=True):
        panel.SetBackgroundColour(self.bgcolor)
        if add_to_list: self.panels.append(panel)

    def createLaserGui(self):

        self.notesizer = wx.BoxSizer(wx.VERTICAL)
        self.notebook = wx.Notebook(self.panel)
        self.notebook.SetBackgroundColour(self.bgcolor)
        page1panel = self.newPanel(self.notebook)
        page2panel = self.newPanel(self.notebook)
        self.mainsizer_page1 = wx.BoxSizer(wx.VERTICAL)
        page1panel1 = self.newPanel(page1panel)
        page1panel2 = self.newPanel(page1panel)
        self.toolbarsizer = MainToolbar(self, page1panel1, use_wrapsizer=True)
        page1panel1.SetSizer(self.toolbarsizer)
        self.mainsizer_page1.Add(page1panel1, 0, wx.EXPAND)

        # self.mainsizer_page1 = wx.BoxSizer(wx.VERTICAL)
        # page1panel1 = self.newPanel(self.panel)
        # self.toolbarsizer = MainToolbar(self, page1panel1, use_wrapsizer=True)
        # page1panel1.SetSizer(self.toolbarsizer)
        # self.mainsizer_page1.Add(page1panel1, 0, wx.EXPAND)

        self.m_staticText2 = wx.StaticText(page1panel, wx.ID_ANY, u"Step 1 使用原噴頭做自動校正", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.mainsizer_page1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_staticline6 = wx.StaticLine(page1panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.mainsizer_page1.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap1 = wx.StaticBitmap(page1panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_bitmap1, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText(page1panel, wx.ID_ANY, u"Auto\nCorrect", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_button4 = wx.Button(page1panel, wx.ID_ANY, u"G28", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.m_button4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
        self.m_button4.Bind(wx.EVT_BUTTON, self.sendG28)

        bSizer3.Add( self.m_button4, 0, wx.ALL, 5 )


        self.mainsizer_page1.Add( bSizer3, 0, wx.EXPAND, 5 )

        self.m_staticline8 = wx.StaticLine(page1panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.mainsizer_page1.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText(page1panel, wx.ID_ANY, u"Step 2 更換雷射噴頭", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        self.mainsizer_page1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_staticline9 = wx.StaticLine(page1panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.mainsizer_page1.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText(page1panel, wx.ID_ANY, u"Step 3 對焦", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        self.mainsizer_page1.Add( self.m_staticText6, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap3 = wx.StaticBitmap(page1panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_bitmap3, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText(page1panel, wx.ID_ANY, u"LASER\nFUNCTION", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.toggleOn = wx.Button(page1panel, 1, u"ON", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.toggleOn, 0, wx.ALL, 5 )
        self.toggleOff = wx.Button(page1panel, 2, u"OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.toggleOff, 0, wx.ALL, 5 )
        self.toggleOff.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        self.toggleOff.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
        self.laserOn = False

        def PressOn(event):
            self.laserOn = True
            self.toggleOn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
            self.toggleOn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
            self.toggleOff.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
            self.toggleOff.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.toggleOn.Bind(wx.EVT_BUTTON, PressOn )

        def PressOff(event):
            self.laserOn = True
            self.toggleOff.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
            self.toggleOff.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
            self.toggleOn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
            self.toggleOn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.toggleOff.Bind(wx.EVT_BUTTON, PressOff )

        self.mainsizer_page1.Add( bSizer5, 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bitmap4 = wx.StaticBitmap(page1panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_bitmap4, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText(page1panel, wx.ID_ANY, u"FOCAL\nDISTANCE", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap( -1 )
        bSizer6.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.fdistspiner = floatspin.FloatSpin(page1panel, -1, value =10.0, increment = 0.1, digits = 1, size = (80, -1))
        bSizer6.Add( self.fdistspiner, 0, flag=wx.ALIGN_CENTER_VERTICAL)

        def update_fdist(event):
            self.fdist = float(self.fdistspiner.GetValue())
            self.update_focaldist(self.fdist)
        self.fdistspiner.Bind(floatspin.EVT_FLOATSPIN, update_fdist)

        self.m_staticText9 = wx.StaticText(page1panel, wx.ID_ANY, u"+ THICKNESS", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer6.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.thickspiner = floatspin.FloatSpin(page1panel, -1, value =0., increment = 0.1, digits = 1, size = (80, -1))
        bSizer6.Add( self.thickspiner, 0, flag=wx.ALIGN_CENTER_VERTICAL)

        def update_thickness(event):
            self.thickness = float(self.thickspiner.GetValue())
        self.thickspiner.Bind(floatspin.EVT_FLOATSPIN, update_thickness)

        self.m_button10 = wx.Button(page1panel, wx.ID_ANY, u"TEST", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button10, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        def TestPressed(event):
            laser_z_dist = float(self.thickspiner.GetValue()) +  float(self.fdistspiner.GetValue())
            self.LaserTest(laser_z_dist)
        self.m_button10.Bind(wx.EVT_BUTTON, TestPressed)

        self.mainsizer_page1.Add( bSizer6, 1, wx.EXPAND, 5 )

        self.m_staticline10 = wx.StaticLine(page1panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.mainsizer_page1.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button_load = wx.Button(page1panel, wx.ID_ANY, u"LOAD", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button_load, 0, wx.ALL, 5 )
        self.m_button_load.Bind(wx.EVT_BUTTON, self.loadpng)

        self.m_button11 = wx.Button(page1panel, wx.ID_ANY, u"PREVIEW", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button11, 0, wx.ALL, 5 )
        self.m_button11.Bind(wx.EVT_BUTTON, self.LaserPreview)

        self.m_button12 = wx.Button(page1panel, wx.ID_ANY, u"START", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button12, 0, wx.ALL, 5 )
        self.m_button12.Bind(wx.EVT_BUTTON, self.LaserStart)

        self.m_button13 = wx.Button(page1panel, wx.ID_ANY, u"PAUSE", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button13, 0, wx.ALL, 5 )
        self.m_button13.Bind(wx.EVT_BUTTON, self.pause)

        self.m_button14 = wx.Button(page1panel, wx.ID_ANY, u"STOP", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button14, 0, wx.ALL, 5 )
        self.m_button14.Bind(wx.EVT_BUTTON, self.off)

        self.m_button15 = wx.Button(page1panel, wx.ID_ANY, u"EXPORT", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_button15, 0, wx.ALL, 5 )



        self.mainsizer_page1.Add( bSizer7, 0, wx.EXPAND, 5 )


        #Page2
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.splitterwindow = wx.SplitterWindow(page2panel, style=wx.SP_3D)
        page2sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        page2sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel1 = self.newPanel(self.splitterwindow)
        page2sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel2 = self.newPanel(self.splitterwindow)
        vizpane = VizPane(self, page2panel1)
        page2sizer1.Add(vizpane, 1, wx.EXPAND)
        page2sizer2.Add(LogPane(self, page2panel2), 1, wx.EXPAND)
        page2panel1.SetSizer(page2sizer1)
        page2panel2.SetSizer(page2sizer2)
        self.splitterwindow.SetMinimumPaneSize(1)
        self.splitterwindow.SetSashGravity(0.5)
        self.splitterwindow.SplitVertically(page2panel1, page2panel2,
                                            self.settings.last_sash_position)
        self.mainsizer.Add(self.splitterwindow, 1, wx.EXPAND)
        page1panel.SetSizer(self.mainsizer_page1)
        page2panel.SetSizer(self.mainsizer)
        self.notesizer.Add(self.notebook, 1, wx.EXPAND)
        self.notebook.AddPage(page1panel, _("Commands"))
        self.notebook.AddPage(page2panel, _("Status"))

        self.panel.SetSizer(self.notesizer)
        self.Bind(wx.EVT_CLOSE, self.kill)

        # self.panel.SetSizerAndFit(self.mainsizer_page1)
        # self.Fit();

        self.panel.SetSizerAndFit(self.notesizer)

        minsize = self.toolbarsizer.GetMinSize()  # lower pane
        minsize[1] = self.notebook.GetSize()[1] + 20
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window
        self.Fit()

    def cerateLaserGuiBackup(self):
        self.notesizer = wx.BoxSizer(wx.VERTICAL)
        self.notebook = wx.Notebook(self.panel)
        self.notebook.SetBackgroundColour(self.bgcolor)
        page1panel = self.newPanel(self.notebook)
        page2panel = self.newPanel(self.notebook)
        self.mainsizer_page1 = wx.BoxSizer(wx.VERTICAL)
        page1panel1 = self.newPanel(page1panel)
        page1panel2 = self.newPanel(page1panel)
        self.toolbarsizer = MainToolbar(self, page1panel1, use_wrapsizer=True)
        page1panel1.SetSizer(self.toolbarsizer)
        self.mainsizer_page1.Add(page1panel1, 0, wx.EXPAND)
        self.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
        page1panel2.SetSizer(self.lowersizer)
        leftsizer = wx.BoxSizer(wx.VERTICAL)
        controls_sizer = ControlsSizer(self, page1panel2, True, False, True)
        leftsizer.Add(controls_sizer, 1, wx.ALIGN_CENTER)
        rightsizer = wx.BoxSizer(wx.VERTICAL)
        # extracontrols = wx.GridBagSizer()
        # add_extra_controls(extracontrols, self, page1panel2, controls_sizer.extra_buttons)
        # rightsizer.AddStretchSpacer()
        # rightsizer.Add(extracontrols, 0, wx.ALIGN_CENTER)
        self.lowersizer.Add(leftsizer, 0, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        self.lowersizer.Add(rightsizer, 1, wx.ALIGN_CENTER)
        self.mainsizer_page1.Add(page1panel2, 1)
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.splitterwindow = wx.SplitterWindow(page2panel, style=wx.SP_3D)
        page2sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel1 = self.newPanel(self.splitterwindow)
        page2sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel2 = self.newPanel(self.splitterwindow)
        vizpane = VizPane(self, page2panel1)
        page2sizer1.Add(vizpane, 1, wx.EXPAND)
        page2sizer2.Add(LogPane(self, page2panel2), 1, wx.EXPAND)
        page2panel1.SetSizer(page2sizer1)
        page2panel2.SetSizer(page2sizer2)
        self.splitterwindow.SetMinimumPaneSize(1)
        self.splitterwindow.SetSashGravity(0.5)
        self.splitterwindow.SplitVertically(page2panel1, page2panel2,
                                            self.settings.last_sash_position)
        self.mainsizer.Add(self.splitterwindow, 1, wx.EXPAND)
        page1panel.SetSizer(self.mainsizer_page1)
        page2panel.SetSizer(self.mainsizer)
        self.notesizer.Add(self.notebook, 1, wx.EXPAND)
        self.notebook.AddPage(page1panel, _("Commands"))
        self.notebook.AddPage(page2panel, _("Status"))

        self.panel.SetSizer(self.notesizer)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
        self.Bind(wx.EVT_CLOSE, self.kill)

        # Custom buttons
        if wx.VERSION > (2, 9):
            self.cbuttonssizer = wx.WrapSizer(wx.HORIZONTAL)
        else:
            self.cbuttonssizer = wx.GridBagSizer()
        self.cbuttonssizer = wx.GridBagSizer()
        self.centerpanel = self.newPanel(page1panel2)
        self.centerpanel.SetSizer(self.cbuttonssizer)
        rightsizer.Add(self.centerpanel, 0, wx.ALIGN_CENTER)
        rightsizer.AddStretchSpacer()

        self.panel.SetSizerAndFit(self.notesizer)

        self.cbuttons_reload()
        minsize = self.lowersizer.GetMinSize()  # lower pane
        minsize[1] = self.notebook.GetSize()[1]
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window
        self.Fit()

    def createTabbedGui(self):
        self.notesizer = wx.BoxSizer(wx.VERTICAL)
        self.notebook = wx.Notebook(self.panel)
        self.notebook.SetBackgroundColour(self.bgcolor)
        page1panel = self.newPanel(self.notebook)
        page2panel = self.newPanel(self.notebook)
        self.mainsizer_page1 = wx.BoxSizer(wx.VERTICAL)
        page1panel1 = self.newPanel(page1panel)
        page1panel2 = self.newPanel(page1panel)
        self.toolbarsizer = MainToolbar(self, page1panel1, use_wrapsizer=True)
        page1panel1.SetSizer(self.toolbarsizer)
        self.mainsizer_page1.Add(page1panel1, 0, wx.EXPAND)
        self.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
        page1panel2.SetSizer(self.lowersizer)
        leftsizer = wx.BoxSizer(wx.VERTICAL)
        controls_sizer = ControlsSizer(self, page1panel2, True)
        leftsizer.Add(controls_sizer, 1, wx.ALIGN_CENTER)
        rightsizer = wx.BoxSizer(wx.VERTICAL)
        extracontrols = wx.GridBagSizer()
        add_extra_controls(extracontrols, self, page1panel2, controls_sizer.extra_buttons)
        rightsizer.AddStretchSpacer()
        rightsizer.Add(extracontrols, 0, wx.ALIGN_CENTER)
        self.lowersizer.Add(leftsizer, 0, wx.ALIGN_CENTER | wx.RIGHT, border=10)
        self.lowersizer.Add(rightsizer, 1, wx.ALIGN_CENTER)
        self.mainsizer_page1.Add(page1panel2, 1)
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.splitterwindow = wx.SplitterWindow(page2panel, style=wx.SP_3D)
        page2sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel1 = self.newPanel(self.splitterwindow)
        page2sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        page2panel2 = self.newPanel(self.splitterwindow)
        vizpane = VizPane(self, page2panel1)
        page2sizer1.Add(vizpane, 1, wx.EXPAND)
        page2sizer2.Add(LogPane(self, page2panel2), 1, wx.EXPAND)
        page2panel1.SetSizer(page2sizer1)
        page2panel2.SetSizer(page2sizer2)
        self.splitterwindow.SetMinimumPaneSize(1)
        self.splitterwindow.SetSashGravity(0.5)
        self.splitterwindow.SplitVertically(page2panel1, page2panel2,
                                            self.settings.last_sash_position)
        self.mainsizer.Add(self.splitterwindow, 1, wx.EXPAND)
        page1panel.SetSizer(self.mainsizer_page1)
        page2panel.SetSizer(self.mainsizer)
        self.notesizer.Add(self.notebook, 1, wx.EXPAND)
        self.notebook.AddPage(page1panel, _("Commands"))
        self.notebook.AddPage(page2panel, _("Status"))
        if self.settings.uimode == _("Tabbed with platers"):
            from printrun.stlplater import StlPlaterPanel
            from printrun.gcodeplater import GcodePlaterPanel

            page3panel = StlPlaterPanel(parent=self.notebook,
                                        callback=self.platecb,
                                        build_dimensions=self.build_dimensions_list,
                                        circular_platform=self.settings.circular_bed,
                                        simarrange_path=self.settings.simarrange_path,
                                        antialias_samples=int(self.settings.antialias3dsamples))
            page4panel = GcodePlaterPanel(parent=self.notebook,
                                          callback=self.platecb,
                                          build_dimensions=self.build_dimensions_list,
                                          circular_platform=self.settings.circular_bed,
                                          antialias_samples=int(self.settings.antialias3dsamples))
            self.registerPanel(page3panel)
            self.registerPanel(page4panel)
            self.notebook.AddPage(page3panel, _("Plater"))
            self.notebook.AddPage(page4panel, _("G-Code Plater"))
        self.panel.SetSizer(self.notesizer)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
        self.Bind(wx.EVT_CLOSE, self.kill)

        # Custom buttons
        if wx.VERSION > (2, 9):
            self.cbuttonssizer = wx.WrapSizer(wx.HORIZONTAL)
        else:
            self.cbuttonssizer = wx.GridBagSizer()
        self.cbuttonssizer = wx.GridBagSizer()
        self.centerpanel = self.newPanel(page1panel2)
        self.centerpanel.SetSizer(self.cbuttonssizer)
        rightsizer.Add(self.centerpanel, 0, wx.ALIGN_CENTER)
        rightsizer.AddStretchSpacer()

        self.panel.SetSizerAndFit(self.notesizer)

        self.cbuttons_reload()
        minsize = self.lowersizer.GetMinSize()  # lower pane
        minsize[1] = self.notebook.GetSize()[1]
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window
        self.Fit()

    def createGui(self, compact=False, mini=False):
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.lowersizer = wx.BoxSizer(wx.HORIZONTAL)
        upperpanel = self.newPanel(self.panel, False)
        self.toolbarsizer = MainToolbar(self, upperpanel)
        lowerpanel = self.newPanel(self.panel)
        upperpanel.SetSizer(self.toolbarsizer)
        lowerpanel.SetSizer(self.lowersizer)
        leftpanel = self.newPanel(lowerpanel)
        left_pane = LeftPaneToggleable(self, leftpanel, [self.lowersizer])
        leftpanel.SetSizer(left_pane)
        left_real_panel = left_pane.panepanel
        controls_panel = self.newPanel(left_real_panel)
        controls_sizer = ControlsSizer(self, controls_panel, mini_mode=mini)
        controls_panel.SetSizer(controls_sizer)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.Add(controls_panel, 1, wx.EXPAND)
        left_pane.set_sizer(left_sizer)
        self.lowersizer.Add(leftpanel, 0, wx.EXPAND)
        if not compact:  # Use a splitterwindow to group viz and log
            rightpanel = self.newPanel(lowerpanel)
            rightsizer = wx.BoxSizer(wx.VERTICAL)
            rightpanel.SetSizer(rightsizer)
            self.splitterwindow = wx.SplitterWindow(rightpanel, style=wx.SP_3D)
            self.splitterwindow.SetMinimumPaneSize(150)
            self.splitterwindow.SetSashGravity(0.8)
            rightsizer.Add(self.splitterwindow, 1, wx.EXPAND)
            vizpanel = self.newPanel(self.splitterwindow)
            logpanel = self.newPanel(self.splitterwindow)
            self.splitterwindow.SplitVertically(vizpanel, logpanel,
                                                self.settings.last_sash_position)
            self.splitterwindow.shrinked = False
        else:
            vizpanel = self.newPanel(lowerpanel)
            logpanel = self.newPanel(left_real_panel)
        viz_pane = VizPane(self, vizpanel)
        # Custom buttons
        if wx.VERSION > (2, 9):
            self.cbuttonssizer = wx.WrapSizer(wx.HORIZONTAL)
        else:
            self.cbuttonssizer = wx.GridBagSizer()
        self.centerpanel = self.newPanel(vizpanel)
        self.centerpanel.SetSizer(self.cbuttonssizer)
        viz_pane.Add(self.centerpanel, 0, flag=wx.ALIGN_CENTER)
        vizpanel.SetSizer(viz_pane)
        if compact:
            log_pane = LogPane(self, logpanel)
        else:
            log_pane = LogPaneToggleable(self, logpanel, [self.lowersizer])
            left_pane.parentsizers.append(self.splitterwindow)
        logpanel.SetSizer(log_pane)
        if not compact:
            self.lowersizer.Add(rightpanel, 1, wx.EXPAND)
        else:
            left_sizer.Add(logpanel, 1, wx.EXPAND)
            self.lowersizer.Add(vizpanel, 1, wx.EXPAND)
        self.mainsizer.Add(upperpanel, 0, wx.EXPAND)
        self.mainsizer.Add(lowerpanel, 1, wx.EXPAND)
        self.panel.SetSizer(self.mainsizer)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.editbutton)
        self.Bind(wx.EVT_CLOSE, self.kill)

        self.mainsizer.Layout()
        # This prevents resizing below a reasonnable value
        # We sum the lowersizer (left pane / viz / log) min size
        # the toolbar height and the statusbar/menubar sizes
        minsize = [0, 0]
        minsize[0] = self.lowersizer.GetMinSize()[0]  # lower pane
        minsize[1] = max(viz_pane.GetMinSize()[1], controls_sizer.GetMinSize()[1])
        minsize[1] += self.toolbarsizer.GetMinSize()[1]  # toolbar height
        displaysize = wx.DisplaySize()
        minsize[0] = min(minsize[0], displaysize[0])
        minsize[1] = min(minsize[1], displaysize[1])
        self.SetMinSize(self.ClientToWindowSize(minsize))  # client to window

        self.cbuttons_reload()

    def gui_set_connected(self):
        #self.xyb.enable()
        #self.zb.enable()
        for control in self.printerControls:
            control.Enable()

    def gui_set_disconnected(self):
        self.printbtn.Disable()
        self.pausebtn.Disable()
        self.recoverbtn.Disable()
        for control in self.printerControls:
            control.Disable()
        #self.xyb.disable()
        #self.zb.disable()


