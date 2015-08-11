# -*- coding: utf-8 -*-

from printrun.gviz import *
from .viz import *

class LaserGviz( Gviz ):
    def __init__(self, parent, size = (200, 200), build_dimensions = [200, 200, 100, 0, 0, 0], grid = (10, 50), extrusion_width = 0.5, bgcolor = "#000000", realparent = None):
        super( LaserGviz, self).__init__(parent, size, build_dimensions, grid, extrusion_width, bgcolor, realparent)
        self.SetMinSize( wx.Size( 600, 600 ))
        self.SetMaxSize( wx.Size( 600, 600 ))



class LaserVizPane(wx.GridBagSizer):
    def __init__(self, root, parentpanel = None):
        super(LaserVizPane, self).__init__(0, 0)
        self.SetFlexibleDirection( wx.BOTH )
        self.SetEmptyCellSize( wx.Size( 114,  103 ))
        self.SetMinSize( wx.Size( 910, 820 ))

        root.gviz = LaserGviz(parentpanel, (300, 300),
                              build_dimensions = root.build_dimensions_list,
                              grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
                              extrusion_width = root.settings.preview_extrusion_width,
                              bgcolor = "#FCEE00")
        root.gviz.SetToolTip(wx.ToolTip(_("Click to examine / edit\n  layers of loaded file")))
        root.gviz.showall = 1
        root.gviz.Bind(wx.EVT_LEFT_DOWN, root.show_viz_window)

        root.gwindow = GvizWindow(build_dimensions = root.build_dimensions_list,
                                       grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
                                       extrusion_width = root.settings.preview_extrusion_width,
                                       bgcolor = root.bgcolor)

        root.gwindow.Bind(wx.EVT_CLOSE, lambda x: root.gwindow.Hide())
        if not isinstance(root.gviz, NoViz):
            self.Add(root.gviz, wx.GBPosition(1,1), wx.GBSpan(6,6))
