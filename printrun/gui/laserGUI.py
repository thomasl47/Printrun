# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.lib.masked import NumCtrl

from .laserGviz import LaserVizPane

###########################################################################
## Class MyPanel3
###########################################################################

WIDTH_TOTAL = 1200
HEIGHT_TOTAL = 700
WIDTH_P1 = 700
WIDTH_P2 = 500

HEIGHT_P3_1 = 90
HEIGHT_P3_2 = 250

BUTTONGPX1 = 30
BUTTONGPX2 = 110

class laserGUI(wx.Panel):
    def __init__(self, parent, root):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(WIDTH_TOTAL, HEIGHT_TOTAL),
                          style=wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.Colour(252, 238, 0))
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gvizPanel = LaserVizPane(root, self)
        mainSizer.Add(self.gvizPanel, 0, 0, 0)

        self.controlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_TOTAL), wx.TAB_TRAVERSAL)
        self.controlPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        ControlSizer = wx.BoxSizer(wx.VERTICAL)

        self.ConnectPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                     wx.TAB_TRAVERSAL)
        self.ConnectPanel.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.ConnectPanel.SetMaxSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        root.toolbarsizer = wx.GridBagSizer(0, 0)
        root.toolbarsizer.SetFlexibleDirection(wx.BOTH)
        root.toolbarsizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        root.toolbarsizer.SetEmptyCellSize(wx.Size(1, 1))

        # Right Panel 1
        root.toolbarsizer.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.ConnectImage = wx.StaticBitmap(self.ConnectPanel, wx.ID_ANY,
                                            wx.Bitmap(u"EditIcon/Icon_Connect-01.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        root.toolbarsizer.Add(self.ConnectImage, wx.GBPosition(10, BUTTONGPX1), wx.GBSpan(10, 40), 0, 0)

        self.ConnectText = wx.StaticText(self.ConnectPanel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.Size(60, -1),
                                         wx.ALIGN_CENTRE)
        self.ConnectText.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        root.toolbarsizer.Add(self.ConnectText, wx.GBPosition(20, 20), wx.GBSpan(4, 60), wx.ALIGN_CENTER_HORIZONTAL, 0)

        root.rescanbtn = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.Size(60, 25),
                                    wx.NO_BORDER)
        root.rescanbtn.SetBackgroundColour(wx.Colour(230, 230, 230))

        root.toolbarsizer.Add(root.rescanbtn, wx.GBPosition(11, BUTTONGPX2), wx.GBSpan(4, 60), 0, 5)

        root.connectbtn = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.Size(80, 25),
                                       wx.NO_BORDER)
        root.connectbtn.SetBackgroundColour(wx.Colour(230, 230, 230))

        root.toolbarsizer.Add(root.connectbtn, wx.GBPosition(17, BUTTONGPX2), wx.GBSpan(4, 80), 0, 5)

        # root.resetbtn = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size(80, 25),
        #                              wx.NO_BORDER)
        # root.resetbtn.SetBackgroundColour(wx.Colour(230, 230, 230))
        #
        # root.toolbarsizer.Add(root.resetbtn, wx.GBPosition(17, 230), wx.GBSpan(4, 80), 0, 5)

        root.serialport = wx.ComboBox(self.ConnectPanel, -1, choices=root.scanserial(), style=wx.CB_DROPDOWN)

        root.toolbarsizer.Add(root.serialport, wx.GBPosition(11, 190), wx.GBSpan(4, 80), 0, 5)

        root.baud = wx.ComboBox(self.ConnectPanel, -1, choices=["2400", "9600", "19200", "38400",
                                                          "57600", "115200", "250000"],
                                style=wx.CB_DROPDOWN, size=(100, -1))
        try:
            root.baud.SetValue("115200")
            root.baud.SetValue(str(root.settings.baudrate))
        except:
            pass

        root.toolbarsizer.Add(root.baud, wx.GBPosition(11, 280), wx.GBSpan(4, 100), 0, 5)

        self.ConnectPanel.SetSizer(root.toolbarsizer)
        self.ConnectPanel.Layout()
        ControlSizer.Add(self.ConnectPanel, 0, wx.ALL, 0)

        # Right Panel 2
        self.CorrectionPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                        wx.TAB_TRAVERSAL)
        self.CorrectionPanel.SetBackgroundColour(wx.Colour(230, 230, 230))

        CorrectionGBSizer = wx.GridBagSizer(0, 0)
        CorrectionGBSizer.SetFlexibleDirection(wx.BOTH)
        CorrectionGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        CorrectionGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        self.CorrectionImage = wx.StaticBitmap(self.CorrectionPanel, wx.ID_ANY,
                                               wx.Bitmap(u"EditIcon/Icon_AutoLevel-01.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        CorrectionGBSizer.Add(self.CorrectionImage, wx.GBPosition(10, 30), wx.GBSpan(10, 40), 0, 0)

        self.CorrectionText = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Auto\nCorrect", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTRE)
        self.CorrectionText.Wrap(-1)
        self.CorrectionText.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))

        CorrectionGBSizer.Add(self.CorrectionText, wx.GBPosition(20, 20), wx.GBSpan(10, 60), wx.ALIGN_CENTER_HORIZONTAL,
                              0)

        self.G29Text = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"G29", wx.DefaultPosition, wx.Size(40,25), 0)
        self.G29Text.Wrap(-1)
        self.G29Text.SetFont(wx.Font(12, 74, 90, 92, False, "Segoe UI Symbol"))

        CorrectionGBSizer.Add(self.G29Text, wx.GBPosition(12, BUTTONGPX2), wx.GBSpan(5, 20), wx.ALIGN_BOTTOM, 5)

        self.CorrectionButton = wx.Button(self.CorrectionPanel, wx.ID_ANY, u"Auto Correct", wx.DefaultPosition,
                                          wx.Size(100, 25), wx.NO_BORDER)
        # self.CorrectionButton.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        self.CorrectionButton.SetForegroundColour(wx.Colour(255, 255, 255))
        self.CorrectionButton.SetBackgroundColour(wx.Colour(0, 146, 69))

        CorrectionGBSizer.Add(self.CorrectionButton, wx.GBPosition(12, 130), wx.GBSpan(5, 100), wx.ALIGN_BOTTOM, 0)

        self.ACText1 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Install Laser Module", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.ACText1.Wrap(-1)
        self.ACText1.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))

        CorrectionGBSizer.Add(self.ACText1, wx.GBPosition(12, 240), wx.GBSpan(5, 50), wx.ALIGN_CENTER_VERTICAL, 5)

        self.ACText2 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"CAUTION!", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        self.ACText2.Wrap(-1)
        self.ACText2.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        self.ACText2.SetForegroundColour(wx.Colour(237, 28, 36))

        CorrectionGBSizer.Add(self.ACText2, wx.GBPosition(18, 240), wx.GBSpan(5, 50), 0, 5)

        self.ACText3 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Use eye protection before continue...",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.ACText3.Wrap(-1)
        self.ACText3.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))
        self.ACText3.SetForegroundColour(wx.Colour(237, 28, 36))

        CorrectionGBSizer.Add(self.ACText3, wx.GBPosition(23, 240), wx.GBSpan(1, 100), 0, 0)

        self.DoneButton = wx.Button(self.CorrectionPanel, wx.ID_ANY, u"Done", wx.DefaultPosition,
                                          wx.Size(60, 25), wx.NO_BORDER)
        self.DoneButton.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        self.DoneButton.SetForegroundColour(wx.Colour(255, 255, 255))
        self.DoneButton.SetBackgroundColour(wx.Colour(251, 176, 59))

        CorrectionGBSizer.Add(self.DoneButton, wx.GBPosition(12, 300), wx.GBSpan(5, 50), wx.ALIGN_BOTTOM, 0)

        self.CorrectionPanel.SetSizer(CorrectionGBSizer)
        self.CorrectionPanel.Layout()
        ControlSizer.Add(self.CorrectionPanel, 0, wx.EXPAND | wx.ALL, 0)

        # Right Panel 3
        self.FocalPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                   wx.TAB_TRAVERSAL)
        self.FocalPanel.SetBackgroundColour(wx.Colour(204, 204, 204))

        FocalGBSizer = wx.GridBagSizer(0, 0)
        FocalGBSizer.SetFlexibleDirection(wx.BOTH)
        FocalGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        FocalGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        self.FocalImage = wx.StaticBitmap(self.FocalPanel, wx.ID_ANY,
                                          wx.Bitmap(u"EditIcon/Icon_Focal-01.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        FocalGBSizer.Add(self.FocalImage, wx.GBPosition(10, 30), wx.GBSpan(10, 40), 0, 0)

        self.FocalText = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Focal\nDistance", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_CENTRE)
        self.FocalText.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        FocalGBSizer.Add(self.FocalText, wx.GBPosition(20, 20), wx.GBSpan(7, 60), 0, 0)

        self.FDText1 = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Laser\nFunction", wx.DefaultPosition,
                                     wx.Size(60, 40), 0)
        self.FDText1.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))

        FocalGBSizer.Add(self.FDText1, wx.GBPosition(12, BUTTONGPX2), wx.GBSpan(10, 60), wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.FDBtnOn = wx.Button(self.FocalPanel, wx.ID_ANY, u"On", wx.DefaultPosition, wx.Size(40, 24), wx.NO_BORDER)
        self.FDBtnOn.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDBtnOn.SetBackgroundColour(wx.Colour(0, 146, 69))

        FocalGBSizer.Add(self.FDBtnOn, wx.GBPosition(12, BUTTONGPX2+60), wx.GBSpan(6, 40), 0, 0)

        self.FDBtnOff = wx.Button(self.FocalPanel, wx.ID_ANY, u"Off", wx.DefaultPosition, wx.Size(40, 24), wx.NO_BORDER)
        self.FDBtnOff.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDBtnOff.SetBackgroundColour(wx.Colour(237, 28, 36))

        FocalGBSizer.Add(self.FDBtnOff, wx.GBPosition(12, BUTTONGPX2+60+40), wx.GBSpan(6, 40), 0, 0)

        self.FDText2 = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Focal\nDistance", wx.DefaultPosition,
                                     wx.Size(60, 40), 0)
        self.FDText2.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))
        FocalGBSizer.Add(self.FDText2, wx.GBPosition(12, 260), wx.GBSpan(10, 60), 0, 0)

        root.FDValue = NumCtrl(self.FocalPanel, wx.ID_ANY, 10, wx.DefaultPosition, size=wx.Size(60, 24), integerWidth=3,
                               fractionWidth = 2)
        FocalGBSizer.Add(root.FDValue, wx.GBPosition(12, 320), wx.GBSpan(6, 60), 0, 0)

        self.FDBtnUp = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                       wx.Bitmap(u"EditIcon/Button_Up.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.Size(24, 18), wx.NO_BORDER)
        self.FDBtnUp.SetMinSize(wx.Size(24, 18))
        self.FDBtnUp.SetMaxSize(wx.Size(24, 18))

        FocalGBSizer.Add(self.FDBtnUp, wx.GBPosition(11, 385), wx.GBSpan(3, 24), 0, 0)

        self.FDBtnDown = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                         wx.Bitmap(u"EditIcon/Button_Down.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                         wx.Size(24, 18), wx.NO_BORDER)
        self.FDBtnDown.SetMinSize(wx.Size(24, 18))
        self.FDBtnDown.SetMaxSize(wx.Size(24, 18))

        FocalGBSizer.Add(self.FDBtnDown, wx.GBPosition(15, 385), wx.GBSpan(3, 24), 0, 0)

        self.FDBtnSet = wx.Button(self.FocalPanel, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.Size(40, 24), wx.NO_BORDER)
        self.FDBtnSet.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDBtnSet.SetBackgroundColour(wx.Colour(251, 176, 59))

        FocalGBSizer.Add(self.FDBtnSet, wx.GBPosition(12, 420), wx.GBSpan(6, 40), 0, 0)

        self.FocalPanel.SetSizer(FocalGBSizer)
        self.FocalPanel.Layout()
        ControlSizer.Add(self.FocalPanel, 0, wx.EXPAND | wx.ALL, 0)

        # Right Panel 4
        self.SetupPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, 250),
                                   wx.TAB_TRAVERSAL)
        self.SetupPanel.SetBackgroundColour(wx.Colour(153, 153, 153))
        self.SetupPanel.SetMinSize(wx.Size(WIDTH_P2, 250))
        self.SetupPanel.SetMaxSize(wx.Size(WIDTH_P2, 250))

        SetupGBSizer = wx.GridBagSizer(0, 0)
        SetupGBSizer.SetFlexibleDirection(wx.BOTH)
        SetupGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        SetupGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        SetupGBSizer.SetMinSize(wx.Size(WIDTH_P2, 250))

        # Right Panel 4-1
        self.ResolutionImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                               wx.Bitmap(u"EditIcon/Icon_Res-01.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.ResolutionImage, wx.GBPosition(20, BUTTONGPX1), wx.GBSpan(10, 40), 0, 0)

        self.ResText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u'Resolution', wx.DefaultPosition, wx.Size(60, -1),
                                     wx.ALIGN_CENTRE)
        self.ResText.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.ResText, wx.GBPosition(30, 20), wx.GBSpan(10, 60), 0, 0)

        self.ResBtnLow = wx.Button(self.SetupPanel, wx.ID_ANY, u"Low", wx.DefaultPosition, wx.Size(60, 25),
                                   wx.NO_BORDER)
        self.ResBtnLow.SetForegroundColour(wx.Colour(0, 0, 0))
        self.ResBtnLow.SetBackgroundColour(wx.Colour(230, 230, 230))

        SetupGBSizer.Add(self.ResBtnLow, wx.GBPosition(24, BUTTONGPX2), wx.GBSpan(5, 60), 0, 0)

        self.ResBtnHigh = wx.Button(self.SetupPanel, wx.ID_ANY, u"High", wx.DefaultPosition, wx.Size(60, 25),
                                    wx.NO_BORDER)
        self.ResBtnHigh.SetForegroundColour(wx.Colour(0, 0, 0))
        self.ResBtnHigh.SetBackgroundColour(wx.Colour(230, 230, 230))

        SetupGBSizer.Add(self.ResBtnHigh, wx.GBPosition(24, BUTTONGPX2+60), wx.GBSpan(5, 60), 0, 0)

        # Right Panel 4-2
        self.SpeedImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                          wx.Bitmap(u"EditIcon/Icon_Speed-01.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.SpeedImage, wx.GBPosition(50, BUTTONGPX1), wx.GBSpan(10, 40), 0, 0)

        self.SpeedText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.Size(60, -1),
                                       wx.ALIGN_CENTRE)
        self.SpeedText.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText, wx.GBPosition(60, 20), wx.GBSpan(10, 60), wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.SpeedText1 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Engrave Speed (mm/s)", wx.DefaultPosition,
                                        wx.Size(140, 15), 0)
        self.SpeedText1.Wrap(-1)
        self.SpeedText1.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText1, wx.GBPosition(51, BUTTONGPX2), wx.GBSpan(3, 140), 0, 0)

        root.EngSpeed = NumCtrl(self.SetupPanel, wx.ID_ANY, 200, wx.DefaultPosition, size=wx.Size(80, 25),
                                        integerWidth=4, autoSize=False)
        SetupGBSizer.Add(root.EngSpeed, wx.GBPosition(54, BUTTONGPX2), wx.GBSpan(6, 80), 0, 0)

        #self.SpeedText2 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm/s", wx.DefaultPosition, wx.Size(30, 20), 0)
        #self.SpeedText2.Wrap(-1)
        #self.SpeedText2.SetForegroundColour(wx.Colour(255, 255, 255))

        #SetupGBSizer.Add(self.SpeedText2, wx.GBPosition(40, BUTTONGPX2+100), wx.GBSpan(4, 30), 0, 0)

        self.SpeedText3 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Travel Speed (mm/s)", wx.DefaultPosition,
                                        wx.Size(140, 15), 0)
        self.SpeedText3.Wrap(-1)
        self.SpeedText3.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText3, wx.GBPosition(51, BUTTONGPX2+140+10), wx.GBSpan(3, 140), 0, 5)

        root.TraSpeed = NumCtrl(self.SetupPanel, wx.ID_ANY, 3000, wx.DefaultPosition, size=wx.Size(80, 25),
                                        integerWidth=4, autoSize=False)
        SetupGBSizer.Add(root.TraSpeed, wx.GBPosition(54, BUTTONGPX2+140+10), wx.GBSpan(6, 80), 0, 5)

        # self.SpeedText4 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm/s", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.SpeedText4.Wrap(-1)
        # self.SpeedText4.SetForegroundColour(wx.Colour(255, 255, 255))
        # SetupGBSizer.Add(self.SpeedText4, wx.GBPosition(40, 410), wx.GBSpan(4, 30), 0, 5)

        # Right Panel 4-3
        self.FDMImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                        wx.Bitmap(u"EditIcon/Icon_FocalWhite-01.png", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.FDMImage, wx.GBPosition(80, BUTTONGPX1), wx.GBSpan(10, 40), 0, 0)

        self.FDMText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Focal Distance\nwith Material", wx.DefaultPosition,
                                     wx.Size(70, -1), wx.ALIGN_CENTRE)
        self.FDMText.Wrap(-1)
        self.FDMText.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.FDMText, wx.GBPosition(90, 15), wx.GBSpan(10, 70), wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.FDMText1 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Focal", wx.DefaultPosition, wx.Size(100, 15), 0)
        self.FDMText1.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.FDMText1, wx.GBPosition(81, BUTTONGPX2), wx.GBSpan(3, 80), 0, 5)

        self.FDMText2 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Thickness", wx.DefaultPosition, wx.Size(100, 15), 0)
        self.FDMText2.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.FDMText2, wx.GBPosition(81, BUTTONGPX2+140+10), wx.GBSpan(3, 100), wx.ALL, 5)

        self.FDMtextCtrl = wx.StaticText(self.SetupPanel, wx.ID_ANY, "10.0", wx.DefaultPosition, wx.Size(80, 30), 0)
        #wx.TextCtrl(self.SetupPanel, wx.ID_ANY, 10.00, wx.DefaultPosition, wx.Size(50, 50), 0)
        self.FDMtextCtrl.SetFont(wx.Font(18, 74, 90, 90, False, "Segoe UI Symbol"))
        self.FDMtextCtrl.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDMtextCtrl.SetBackgroundColour(wx.Colour(153, 153, 153))

        SetupGBSizer.Add(self.FDMtextCtrl, wx.GBPosition(84, BUTTONGPX2), wx.GBSpan(15, 80), 0, 0)

        self.FDMPlusImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                            wx.Bitmap(u"EditIcon/Icon_Plus.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.FDMPlusImage, wx.GBPosition(84, BUTTONGPX2+110), wx.GBSpan(5, 25), 0, 5)

        root.Thickness = NumCtrl(self.SetupPanel, wx.ID_ANY, 0, wx.DefaultPosition, size=wx.Size(110, 25),
                                        integerWidth=3, fractionWidth=2, autoSize=False)
        SetupGBSizer.Add( root.Thickness, wx.GBPosition(84, BUTTONGPX2+140+10), wx.GBSpan(8, 100), 0, 0)

        self.SetupPanel.SetSizer(SetupGBSizer)
        self.SetupPanel.Layout()
        ControlSizer.Add(self.SetupPanel, 0, 0, 0)

        # Right Panel 5
        self.ImportPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, 90),
                                    wx.TAB_TRAVERSAL)
        self.ImportPanel.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.ImportPanel.SetMinSize(wx.Size(WIDTH_P2, 90))
        self.ImportPanel.SetMaxSize(wx.Size(WIDTH_P2, 90))

        ImpotyGBSizer = wx.GridBagSizer(0, 0)
        ImpotyGBSizer.SetFlexibleDirection(wx.BOTH)
        ImpotyGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ImpotyGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        ImpotyGBSizer.SetMinSize(wx.Size(115, 90))
        self.ImportImage = wx.StaticBitmap(self.ImportPanel, wx.ID_ANY,
                                           wx.Bitmap(u"EditIcon/Icon_Import-01.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        ImpotyGBSizer.Add(self.ImportImage, wx.GBPosition(10, BUTTONGPX1), wx.GBSpan(10, 40), 0, 0)

        self.ImportText = wx.StaticText(self.ImportPanel, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.Size(60, -1),
                                        wx.ALIGN_CENTRE)
        self.ImportText.Wrap(-1)
        self.ImportText.SetForegroundColour(wx.Colour(255, 255, 255))

        ImpotyGBSizer.Add(self.ImportText, wx.GBPosition(20, 20), wx.GBSpan(10, 60), 0, 0)

        root.FilePathLabel = wx.StaticText(self.ImportPanel, wx.ID_ANY, "", wx.DefaultPosition, wx.Size(280, 25), 0)
        #self.FilePathText.SetFont(wx.Font(18, 74, 90, 90, False, "Segoe UI Symbol"))
        root.FilePathLabel.SetForegroundColour(wx.Colour(0, 0, 0))
        root.FilePathLabel.SetBackgroundColour(wx.Colour(255, 255, 255))
        root.FilePathLabel.SetMaxSize(wx.Size(280, 25))
        root.FilePathLabel.SetMinSize(wx.Size(280, 25))
        #root.FilePathLabel.SetWrap(1)
        ImpotyGBSizer.Add(root.FilePathLabel, wx.GBPosition(14, BUTTONGPX2), wx.GBSpan(5, 280), 0, 0)

        self.ImportBtn = wx.Button(self.ImportPanel, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.Size(60, 25),
                                   wx.NO_BORDER)
        self.ImportBtn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.ImportBtn.SetBackgroundColour(wx.Colour(230, 230, 230))
        ImpotyGBSizer.Add(self.ImportBtn, wx.GBPosition(14, BUTTONGPX2+280+5), wx.GBSpan(5, 60), 0, 0)

        self.ImportPanel.SetSizer(ImpotyGBSizer)
        self.ImportPanel.Layout()
        ControlSizer.Add(self.ImportPanel, 0, wx.EXPAND, 0)

        # Right Panel 6
        self.ActionPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(WIDTH_P2, HEIGHT_P3_1),
                                    wx.TAB_TRAVERSAL)
        self.ActionPanel.SetBackgroundColour(wx.Colour(102, 102, 102))
        self.ActionPanel.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))
        self.ActionPanel.SetMaxSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        ActionGBSizer = wx.GridBagSizer(0, 0)
        ActionGBSizer.SetFlexibleDirection(wx.BOTH)
        ActionGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ActionGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        ActionGBSizer.SetMinSize(wx.Size(WIDTH_P2, HEIGHT_P3_1))

        # Preview btn
        BTNXPOS = BUTTONGPX1
        BTNWIDTH = 40
        BTNXSPACE = 40
        self.ActPreviewBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                             wx.Bitmap(u"EditIcon/Icon_Preview_MouseOn-01.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(40, 40), wx.NO_BORDER)
        ActionGBSizer.Add(self.ActPreviewBtn, wx.GBPosition(20, BTNXPOS), wx.GBSpan(10, 40), 0, 0)

        self.ActPreviewLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Preview", wx.DefaultPosition,
                                             wx.Size(60, 20), wx.ALIGN_CENTRE)
        self.ActPreviewLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActPreviewLabel, wx.GBPosition(30, BTNXPOS-10), wx.GBSpan(10, 60), 0, 5)

        # Start btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        root.printbtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                           wx.Bitmap(u"EditIcon/Icon_Start_Preview-01.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.Size(40, 40), wx.NO_BORDER)
        root.printbtn.SetBackgroundColour( wx.Colour(128, 128, 0))
        ActionGBSizer.Add(root.printbtn, wx.GBPosition(20, BTNXPOS), wx.GBSpan(10, 50), 0, 0)

        self.ActStartLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size(60, 20),
                                           wx.ALIGN_CENTRE)
        self.ActStartLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActStartLabel, wx.GBPosition(30, BTNXPOS-10), wx.GBSpan(10, 60), 0, 5)

        # Pause btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        root.pausebtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                           wx.Bitmap(u"EditIcon/Icon_Pause-01.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.Size(40, 40), wx.NO_BORDER)
        ActionGBSizer.Add(root.pausebtn, wx.GBPosition(20, BTNXPOS), wx.GBSpan(10, 50), 0, 5)

        self.ActPauseLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.Size(60, 20),
                                           wx.ALIGN_CENTRE)
        self.ActPauseLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActPauseLabel, wx.GBPosition(30, BTNXPOS-10), wx.GBSpan(10, 60), 0, 5)

        # Stop btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        root.offbtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                          wx.Bitmap(u"EditIcon/Icon_Stop-01.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(40, 40), wx.NO_BORDER)
        ActionGBSizer.Add(root.offbtn, wx.GBPosition(20, BTNXPOS), wx.GBSpan(10, 50), 0, 5)

        self.ActStopLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size(60, 20),
                                          wx.ALIGN_CENTRE)
        self.ActStopLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActStopLabel, wx.GBPosition(30, BTNXPOS-10), wx.GBSpan(10, 60), 0, 5)

        # Export btn
        BTNXPOS += BTNWIDTH+BTNXSPACE
        self.ActExportBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                            wx.Bitmap(u"EditIcon/Icon_Export-01.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.Size(40, 40), wx.NO_BORDER)
        ActionGBSizer.Add(self.ActExportBtn, wx.GBPosition(20, BTNXPOS), wx.GBSpan(10, 50), 0, 5)

        self.ActExportLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.Size(60, 20),
                                            wx.ALIGN_CENTRE)
        self.ActExportLabel.SetForegroundColour(wx.Colour(255, 255, 255))
        ActionGBSizer.Add(self.ActExportLabel, wx.GBPosition(30, BTNXPOS-10), wx.GBSpan(10, 60), 0, 5)

        # self.blubIcon = wx.StaticBitmap(self.ActionPanel, wx.ID_ANY,
        #                                 wx.Bitmap(u"EditIcon/Bulb.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
        #                                 wx.DefaultSize, 0)
        # ActionGBSizer.Add(self.blubIcon, wx.GBPosition(5, 450), wx.GBSpan(100, 80), 0, 5)

        self.ActionPanel.SetSizer(ActionGBSizer)
        self.ActionPanel.Layout()
        ControlSizer.Add(self.ActionPanel, 0, wx.EXPAND, 0)

        self.controlPanel.SetSizer(ControlSizer)
        self.controlPanel.Layout()
        mainSizer.Add(self.controlPanel, 0, 0, 0)

        self.rightcolorpanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(10, 820), wx.TAB_TRAVERSAL)
        self.rightcolorpanel.SetBackgroundColour(wx.Colour(252, 238, 0))
        self.rightcolorpanel.SetMinSize(wx.Size(10, 820))
        self.rightcolorpanel.SetMaxSize(wx.Size(10, 820))

        mainSizer.Add(self.rightcolorpanel, 0, 0, 0)

        self.SetSizer(mainSizer)
        self.Layout()

        self.BindCommand(root)

    def __del__(self):
        pass

    def BindCommand(self, root):
        root.rescanbtn.Bind(wx.EVT_BUTTON, root.rescanports)
        root.connectbtn.Bind(wx.EVT_BUTTON, root.connect)
        # root.resetbtn.Bind(wx.EVT_BUTTON, root.reset)

        def sendGCodeCommand(command):
            def sendCmd(event):
                root.sendGCodeCommand(command)
            return sendCmd

        self.CorrectionButton.Bind(wx.EVT_BUTTON, sendGCodeCommand('G29'))
        self.DoneButton.Bind(wx.EVT_BUTTON, sendGCodeCommand('G28'))

        self.FDBtnOn.Bind(wx.EVT_BUTTON, sendGCodeCommand('M03'))
        self.FDBtnOff.Bind(wx.EVT_BUTTON, sendGCodeCommand('M05'))

        def addValue(value):
            def addvalue(event):
                newValue = str(float(root.FDValue.GetValue())+float(value))
                root.FDValue.SetValue(newValue)
                root.FDValue.Refresh()
                self.FDMtextCtrl.SetLabel(newValue)
                root.sendGCodeCommand('G0 Z'+newValue)
            return addvalue
        #root.FDValue.Bind(wx.EVT_LEAVE_WINDOW, addValue(0))
        self.FDBtnUp.Bind(wx.EVT_BUTTON, addValue(0.1))
        self.FDBtnDown.Bind(wx.EVT_BUTTON, addValue(-0.1))
        #self.FDBtnSet.Bind(wx.EVT_BUTTON, root.sendZFocalDist)

        self.ResBtnHigh.Bind(wx.EVT_BUTTON, root.setHighResolution)
        self.ResBtnLow.Bind(wx.EVT_BUTTON, root.setLowResolution)

        self.ImportBtn.Bind(wx.EVT_BUTTON, root.loadpng)

        self.ActPreviewBtn.Bind(wx.EVT_BUTTON, root.LaserPreview)
        root.printbtn.Bind(wx.EVT_BUTTON, root.LaserStart)
        root.pausebtn.Bind(wx.EVT_BUTTON, root.pause)
        root.offbtn.Bind(wx.EVT_BUTTON, root.off)
        self.ActExportBtn.Bind(wx.EVT_BUTTON, root.savefile)

