# -*- coding: utf-8 -*-

from printrun.gviz import *
from .viz import *
from .log import LogPane

class LaserGviz( Gviz ):
    def __init__(self, parent, size = (200, 200), build_dimensions = [200, 200, 100, 0, 0, 0], grid = (10, 50), extrusion_width = 0.5, bgcolor = "#000000", realparent = None):
        super( LaserGviz, self).__init__(parent, size, build_dimensions, grid, extrusion_width, bgcolor, realparent)
        self.SetMinSize( wx.Size( 560, 560 ))
        self.SetMaxSize( wx.Size( 560, 560 ))

    def repaint_everything(self):
        width = self.scale[0] * self.build_dimensions[0]
        height = self.scale[1] * self.build_dimensions[1]
        self.blitmap = wx.EmptyBitmap(width + 1, height + 1, -1)
        dc = wx.MemoryDC()
        dc.SelectObject(self.blitmap)
        dc.SetBackground(wx.Brush((250, 250, 200)))
        dc.Clear()
        dc.SetPen(wx.Pen(wx.Colour(180, 180, 150)))
        # for grid_unit in self.grid:
        #     if grid_unit > 0:
        #         for x in xrange(int(self.build_dimensions[0] / grid_unit) + 1):
        #             draw_x = self.scale[0] * x * grid_unit
        #             dc.DrawLine(draw_x, 0, draw_x, height)
        #         for y in xrange(int(self.build_dimensions[1] / grid_unit) + 1):
        #             draw_y = self.scale[1] * (self.build_dimensions[1] - y * grid_unit)
        #             dc.DrawLine(0, draw_y, width, draw_y)
        #     dc.SetPen(wx.Pen(wx.Colour(0, 0, 0)))

        if not self.showall:
            # Draw layer gauge
            dc.SetBrush(wx.Brush((43, 144, 255)))
            dc.DrawRectangle(width - 15, 0, 15, height)
            dc.SetBrush(wx.Brush((0, 255, 0)))
            if self.layers:
                dc.DrawRectangle(width - 14, (1.0 - (1.0 * (self.layerindex + 1)) / len(self.layers)) * height, 13, height - 1)

        if self.showall:
            for i in range(len(self.layersz)):
                self.painted_layers.add(i)
                self._drawlines(dc, self.lines[i], self.pens[i])
                self._drawarcs(dc, self.arcs[i], self.arcpens[i])
            dc.SelectObject(wx.NullBitmap)
            return

        if self.layerindex < len(self.layers) and self.layerindex in self.lines:
            for layer_i in range(max(0, self.layerindex - 6), self.layerindex):
                self._drawlines(dc, self.lines[layer_i], self.fades[self.layerindex - layer_i - 1])
                self._drawarcs(dc, self.arcs[layer_i], self.fades[self.layerindex - layer_i - 1])
            self._drawlines(dc, self.lines[self.layerindex], self.pens[self.layerindex])
            self._drawarcs(dc, self.arcs[self.layerindex], self.arcpens[self.layerindex])

        self._drawlines(dc, self.hilight, self.hlpen)
        self._drawarcs(dc, self.hilightarcs, self.hlpen)

        self.paint_hilights(dc)

        dc.SelectObject(wx.NullBitmap)

class LaserVizPane(wx.GridBagSizer):
    def __init__(self, root, parentpanel = None):
        super(LaserVizPane, self).__init__(0, 0)
        self.SetFlexibleDirection(wx.BOTH)
        self.SetEmptyCellSize( wx.Size(70, 70))
        self.SetMinSize( wx.Size(700, 700))

        root.gviz = LaserGviz(parentpanel, (560, 560),
                              build_dimensions = [200, 200, 100, -100, -100, 0],
                              grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
                              extrusion_width = root.settings.preview_extrusion_width,
                              bgcolor = "#FCEE00")

        #root.gviz.SetToolTip(wx.ToolTip(_("Click to examine / edit\n  layers of loaded file")))
        root.gviz.showall = 1
        #root.gviz.Bind(wx.EVT_LEFT_DOWN, root.show_viz_window)

        root.gwindow = GvizWindow(build_dimensions = root.build_dimensions_list,
                                       grid = (root.settings.preview_grid_step1, root.settings.preview_grid_step2),
                                       extrusion_width = root.settings.preview_extrusion_width,
                                       bgcolor = root.bgcolor)

        root.gwindow.Bind(wx.EVT_CLOSE, lambda x: root.gwindow.Hide())
        if not isinstance(root.gviz, NoViz):
            self.Add(root.gviz, wx.GBPosition(1,1), wx.GBSpan(8,8))

        root.laserLogpanel = LogPane(root, parentpanel)
        root.laserLogpanel.SetMinSize( wx.Size(-1, 80))
        self.Add(root.laserLogpanel, wx.GBPosition(10,1), wx.GBSpan(1,8), wx.EXPAND)
