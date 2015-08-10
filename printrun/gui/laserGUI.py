# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel3
###########################################################################

class laserGUI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1440, 820),
                          style=wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.gvizPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(910, 820), wx.TAB_TRAVERSAL)
        self.gvizPanel.SetBackgroundColour(wx.Colour(252, 238, 0))

        mainSizer.Add(self.gvizPanel, 0, 0, 0)

        self.controlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 820), wx.TAB_TRAVERSAL)
        self.controlPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        ControlSizer = wx.BoxSizer(wx.VERTICAL)

        self.ConnectPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 115),
                                     wx.TAB_TRAVERSAL)
        self.ConnectPanel.Enable(False)
        self.ConnectPanel.SetMinSize(wx.Size(520, 115))
        self.ConnectPanel.SetMaxSize(wx.Size(520, 115))

        ConnectGBSizer1 = wx.GridBagSizer(0, 0)
        ConnectGBSizer1.SetFlexibleDirection(wx.BOTH)
        ConnectGBSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ConnectGBSizer1.SetEmptyCellSize(wx.Size(1, 1))

        ConnectGBSizer1.SetMinSize(wx.Size(520, 115))
        self.ConnectImage = wx.StaticBitmap(self.ConnectPanel, wx.ID_ANY,
                                            wx.Bitmap(u"EditIcon/Icon_Connect-01.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        ConnectGBSizer1.Add(self.ConnectImage, wx.GBPosition(10, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.PortButton = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.Size(60, 25),
                                    wx.NO_BORDER)
        self.PortButton.SetBackgroundColour(wx.Colour(230, 230, 230))

        ConnectGBSizer1.Add(self.PortButton, wx.GBPosition(12, 140), wx.GBSpan(4, 60), 0, 5)

        self.ConnectButton = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.Size(80, 25),
                                       wx.NO_BORDER)
        self.ConnectButton.SetBackgroundColour(wx.Colour(230, 230, 230))

        ConnectGBSizer1.Add(self.ConnectButton, wx.GBPosition(18, 140), wx.GBSpan(4, 80), 0, 5)

        self.ResetButton = wx.Button(self.ConnectPanel, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size(80, 25),
                                     wx.NO_BORDER)
        self.ResetButton.SetBackgroundColour(wx.Colour(230, 230, 230))

        ConnectGBSizer1.Add(self.ResetButton, wx.GBPosition(18, 230), wx.GBSpan(4, 80), 0, 5)

        self.ConnectText = wx.StaticText(self.ConnectPanel, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize,
                                         wx.ALIGN_CENTRE)
        self.ConnectText.Wrap(-1)
        ConnectGBSizer1.Add(self.ConnectText, wx.GBPosition(20, 30), wx.GBSpan(10, 50), wx.ALIGN_CENTER_HORIZONTAL, 0)

        PortBoxChoices = []
        self.PortBox = wx.ComboBox(self.ConnectPanel, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                   PortBoxChoices, 0)
        ConnectGBSizer1.Add(self.PortBox, wx.GBPosition(12, 205), wx.GBSpan(4, 100), 0, 5)

        BoundRateBoxChoices = []
        self.BoundRateBox = wx.ComboBox(self.ConnectPanel, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                        BoundRateBoxChoices, 0)
        ConnectGBSizer1.Add(self.BoundRateBox, wx.GBPosition(12, 325), wx.GBSpan(4, 100), 0, 5)

        self.ConnectPanel.SetSizer(ConnectGBSizer1)
        self.ConnectPanel.Layout()
        ControlSizer.Add(self.ConnectPanel, 0, wx.ALL, 0)

        self.CorrectionPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 115),
                                        wx.TAB_TRAVERSAL)
        self.CorrectionPanel.SetBackgroundColour(wx.Colour(230, 230, 230))

        CorrectionGBSizer = wx.GridBagSizer(0, 0)
        CorrectionGBSizer.SetFlexibleDirection(wx.BOTH)
        CorrectionGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        CorrectionGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        self.CorrectionImage = wx.StaticBitmap(self.CorrectionPanel, wx.ID_ANY,
                                               wx.Bitmap(u"EditIcon/Icon_AutoLevel-01.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        CorrectionGBSizer.Add(self.CorrectionImage, wx.GBPosition(10, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.CorrectionText = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Auto\nCorrect", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTRE)
        self.CorrectionText.Wrap(-1)
        self.CorrectionText.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))

        CorrectionGBSizer.Add(self.CorrectionText, wx.GBPosition(20, 30), wx.GBSpan(10, 50), wx.ALIGN_CENTER_HORIZONTAL,
                              0)

        self.G29Text = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"G29", wx.DefaultPosition, wx.DefaultSize, 0)
        self.G29Text.Wrap(-1)
        self.G29Text.SetFont(wx.Font(12, 74, 90, 92, False, "Segoe UI Symbol"))

        CorrectionGBSizer.Add(self.G29Text, wx.GBPosition(15, 140), wx.GBSpan(5, 20), wx.ALIGN_BOTTOM, 5)

        self.ACText1 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Install Laser Module", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.ACText1.Wrap(-1)
        self.ACText1.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))

        CorrectionGBSizer.Add(self.ACText1, wx.GBPosition(15, 290), wx.GBSpan(5, 1), wx.ALIGN_CENTER_VERTICAL, 5)

        self.CorrectionButton = wx.Button(self.CorrectionPanel, wx.ID_ANY, u"Auto Correct", wx.DefaultPosition,
                                          wx.Size(100, 25), wx.NO_BORDER)
        self.CorrectionButton.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        self.CorrectionButton.SetForegroundColour(wx.Colour(255, 255, 255))
        self.CorrectionButton.SetBackgroundColour(wx.Colour(0, 146, 69))

        CorrectionGBSizer.Add(self.CorrectionButton, wx.GBPosition(15, 170), wx.GBSpan(5, 100), wx.ALIGN_BOTTOM, 0)

        self.ACText2 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"CAUTION!", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        self.ACText2.Wrap(-1)
        self.ACText2.SetFont(wx.Font(9, 74, 90, 92, False, "Segoe UI Symbol"))
        self.ACText2.SetForegroundColour(wx.Colour(237, 28, 36))

        CorrectionGBSizer.Add(self.ACText2, wx.GBPosition(20, 290), wx.GBSpan(5, 1), 0, 5)

        self.ACText3 = wx.StaticText(self.CorrectionPanel, wx.ID_ANY, u"Use eye protection before continue...",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.ACText3.Wrap(-1)
        self.ACText3.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))
        self.ACText3.SetForegroundColour(wx.Colour(237, 28, 36))

        CorrectionGBSizer.Add(self.ACText3, wx.GBPosition(25, 290), wx.GBSpan(1, 1), 0, 0)

        self.CorrectionPanel.SetSizer(CorrectionGBSizer)
        self.CorrectionPanel.Layout()
        ControlSizer.Add(self.CorrectionPanel, 0, wx.EXPAND | wx.ALL, 0)

        self.FocalPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 115),
                                   wx.TAB_TRAVERSAL)
        self.FocalPanel.SetBackgroundColour(wx.Colour(204, 204, 204))

        FocalGBSizer = wx.GridBagSizer(0, 0)
        FocalGBSizer.SetFlexibleDirection(wx.BOTH)
        FocalGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        FocalGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        self.FocalImage = wx.StaticBitmap(self.FocalPanel, wx.ID_ANY,
                                          wx.Bitmap(u"EditIcon/Icon_Focal-01.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        FocalGBSizer.Add(self.FocalImage, wx.GBPosition(10, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.FocalText = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Focal\nDistance", wx.DefaultPosition,
                                       wx.DefaultSize, wx.ALIGN_CENTRE)
        self.FocalText.Wrap(-1)
        FocalGBSizer.Add(self.FocalText, wx.GBPosition(20, 30), wx.GBSpan(10, 50), wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.FDText1 = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Laser Function", wx.DefaultPosition,
                                     wx.Size(100, 20), 0)
        self.FDText1.Wrap(-1)
        self.FDText1.SetFont(wx.Font(9, 74, 90, 90, False, "Segoe UI Symbol"))

        FocalGBSizer.Add(self.FDText1, wx.GBPosition(13, 140), wx.GBSpan(3, 100), 0, 5)

        self.FDText2 = wx.StaticText(self.FocalPanel, wx.ID_ANY, u"Focal Distance", wx.DefaultPosition,
                                     wx.Size(100, 20), 0)
        self.FDText2.Wrap(-1)
        FocalGBSizer.Add(self.FDText2, wx.GBPosition(20, 140), wx.GBSpan(3, 100), 0, 5)

        self.FDBtnOn = wx.Button(self.FocalPanel, wx.ID_ANY, u"On", wx.DefaultPosition, wx.Size(60, 25), wx.NO_BORDER)
        self.FDBtnOn.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDBtnOn.SetBackgroundColour(wx.Colour(0, 146, 69))

        FocalGBSizer.Add(self.FDBtnOn, wx.GBPosition(12, 240), wx.GBSpan(4, 60), 0, 5)

        self.FDValue = wx.TextCtrl(self.FocalPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, 25), 0)
        FocalGBSizer.Add(self.FDValue, wx.GBPosition(19, 240), wx.GBSpan(4, 60), 0, 5)

        self.FDBtnUp = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                       wx.Bitmap(u"EditIcon/Button_Up.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                       wx.Size(24, 18), wx.BU_AUTODRAW)
        self.FDBtnUp.SetMinSize(wx.Size(24, 18))
        self.FDBtnUp.SetMaxSize(wx.Size(24, 18))

        FocalGBSizer.Add(self.FDBtnUp, wx.GBPosition(18, 310), wx.GBSpan(2, 24), 0, 0)

        self.FDBtnDown = wx.BitmapButton(self.FocalPanel, wx.ID_ANY,
                                         wx.Bitmap(u"EditIcon/Button_Down.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                         wx.Size(24, 18), wx.BU_AUTODRAW)
        self.FDBtnDown.SetMinSize(wx.Size(24, 18))
        self.FDBtnDown.SetMaxSize(wx.Size(24, 18))

        FocalGBSizer.Add(self.FDBtnDown, wx.GBPosition(21, 310), wx.GBSpan(2, 24), 0, 0)

        self.FDBtnOff = wx.Button(self.FocalPanel, wx.ID_ANY, u"Off", wx.DefaultPosition, wx.Size(60, 25), wx.NO_BORDER)
        self.FDBtnOff.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDBtnOff.SetBackgroundColour(wx.Colour(237, 28, 36))

        FocalGBSizer.Add(self.FDBtnOff, wx.GBPosition(12, 305), wx.GBSpan(4, 60), 0, 5)

        self.FDBtnSet = wx.Button(self.FocalPanel, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.Size(60, 25), wx.NO_BORDER)
        self.FDBtnSet.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDBtnSet.SetBackgroundColour(wx.Colour(251, 176, 59))

        FocalGBSizer.Add(self.FDBtnSet, wx.GBPosition(19, 350), wx.GBSpan(4, 60), 0, 5)

        self.FocalPanel.SetSizer(FocalGBSizer)
        self.FocalPanel.Layout()
        ControlSizer.Add(self.FocalPanel, 0, wx.EXPAND | wx.ALL, 0)

        self.SetupPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 270),
                                   wx.TAB_TRAVERSAL)
        self.SetupPanel.SetBackgroundColour(wx.Colour(153, 153, 153))
        self.SetupPanel.Enable(False)
        self.SetupPanel.SetMinSize(wx.Size(520, 270))
        self.SetupPanel.SetMaxSize(wx.Size(520, 270))

        SetupGBSizer = wx.GridBagSizer(0, 0)
        SetupGBSizer.SetFlexibleDirection(wx.BOTH)
        SetupGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        SetupGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        SetupGBSizer.SetMinSize(wx.Size(520, 270))
        self.ResolutionImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                               wx.Bitmap(u"EditIcon/Icon_Res-01.png", wx.BITMAP_TYPE_ANY),
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.ResolutionImage, wx.GBPosition(10, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.ResText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Resolution", wx.DefaultPosition, wx.DefaultSize,
                                     wx.ALIGN_CENTRE)
        self.ResText.Wrap(-1)
        self.ResText.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.ResText, wx.GBPosition(20, 30), wx.GBSpan(10, 50), 0, 0)

        self.ResBtnLow = wx.Button(self.SetupPanel, wx.ID_ANY, u"Low", wx.DefaultPosition, wx.Size(60, 25),
                                   wx.NO_BORDER)
        self.ResBtnLow.SetForegroundColour(wx.Colour(0, 0, 0))
        self.ResBtnLow.SetBackgroundColour(wx.Colour(230, 230, 230))

        SetupGBSizer.Add(self.ResBtnLow, wx.GBPosition(14, 140), wx.GBSpan(5, 60), 0, 5)

        self.ResBtnHigh = wx.Button(self.SetupPanel, wx.ID_ANY, u"High", wx.DefaultPosition, wx.Size(60, 25),
                                    wx.NO_BORDER)
        self.ResBtnHigh.SetForegroundColour(wx.Colour(0, 0, 0))
        self.ResBtnHigh.SetBackgroundColour(wx.Colour(230, 230, 230))

        SetupGBSizer.Add(self.ResBtnHigh, wx.GBPosition(14, 205), wx.GBSpan(5, 60), 0, 5)

        self.SpeedImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                          wx.Bitmap(u"EditIcon/Icon_Speed-01.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.SpeedImage, wx.GBPosition(35, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.SpeedText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.DefaultSize,
                                       wx.ALIGN_CENTRE)
        self.SpeedText.Wrap(-1)
        self.SpeedText.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText, wx.GBPosition(45, 30), wx.GBSpan(10, 50), wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SpeedText1 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Engrave Speed", wx.DefaultPosition,
                                        wx.Size(100, 15), 0)
        self.SpeedText1.Wrap(-1)
        self.SpeedText1.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText1, wx.GBPosition(36, 140), wx.GBSpan(3, 80), 0, 5)

        self.SpeedText2 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm/s", wx.DefaultPosition, wx.DefaultSize, 0)
        self.SpeedText2.Wrap(-1)
        self.SpeedText2.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText2, wx.GBPosition(40, 240), wx.GBSpan(4, 30), 0, 5)

        self.SpeedText3 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Travel Speed", wx.DefaultPosition,
                                        wx.Size(100, 15), 0)
        self.SpeedText3.Wrap(-1)
        self.SpeedText3.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText3, wx.GBPosition(36, 300), wx.GBSpan(3, 100), 0, 5)

        self.SpeedText4 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"mm/s", wx.DefaultPosition, wx.DefaultSize, 0)
        self.SpeedText4.Wrap(-1)
        self.SpeedText4.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.SpeedText4, wx.GBPosition(40, 410), wx.GBSpan(4, 30), 0, 5)

        self.FDMImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                        wx.Bitmap(u"EditIcon/Icon_FocalWhite-01.png", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.FDMImage, wx.GBPosition(60, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.FDMText = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Focal Distance\nwith Material", wx.DefaultPosition,
                                     wx.DefaultSize, wx.ALIGN_CENTRE)
        self.FDMText.Wrap(-1)
        self.FDMText.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.FDMText, wx.GBPosition(70, 20), wx.GBSpan(10, 70), 0, 5)

        self.FDMText1 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Focal", wx.DefaultPosition, wx.Size(100, 15), 0)
        self.FDMText1.Wrap(-1)
        self.FDMText1.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.FDMText1, wx.GBPosition(61, 140), wx.GBSpan(3, 80), 0, 5)

        self.FDMText2 = wx.StaticText(self.SetupPanel, wx.ID_ANY, u"Thickness", wx.DefaultPosition, wx.Size(100, 15), 0)
        self.FDMText2.Wrap(-1)
        self.FDMText2.SetForegroundColour(wx.Colour(255, 255, 255))

        SetupGBSizer.Add(self.FDMText2, wx.GBPosition(61, 300), wx.GBSpan(3, 80), wx.ALL, 5)

        self.FDMtextCtrl = wx.TextCtrl(self.SetupPanel, wx.ID_ANY, u"8.5", wx.DefaultPosition, wx.Size(50, 50), 0)
        self.FDMtextCtrl.SetFont(wx.Font(18, 74, 90, 90, False, "Segoe UI Symbol"))
        self.FDMtextCtrl.SetForegroundColour(wx.Colour(255, 255, 255))
        self.FDMtextCtrl.SetBackgroundColour(wx.Colour(153, 153, 153))

        SetupGBSizer.Add(self.FDMtextCtrl, wx.GBPosition(64, 140), wx.GBSpan(15, 50), 0, 5)

        self.FDMPlusImage = wx.StaticBitmap(self.SetupPanel, wx.ID_ANY,
                                            wx.Bitmap(u"EditIcon/Icon_Plus.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        SetupGBSizer.Add(self.FDMPlusImage, wx.GBPosition(66, 260), wx.GBSpan(5, 25), 0, 5)

        self.EngSpeedtextCtrl = wx.TextCtrl(self.SetupPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(110, 25), 0)
        SetupGBSizer.Add(self.EngSpeedtextCtrl, wx.GBPosition(39, 140), wx.GBSpan(6, 100), 0, 5)

        self.TraSpeedtextCtrl = wx.TextCtrl(self.SetupPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(110, 25), 0)
        SetupGBSizer.Add(self.TraSpeedtextCtrl, wx.GBPosition(39, 300), wx.GBSpan(6, 100), 0, 5)

        self.ThicknesstextCtrl = wx.TextCtrl(self.SetupPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(110, 25), 0)
        SetupGBSizer.Add(self.ThicknesstextCtrl, wx.GBPosition(65, 300), wx.GBSpan(8, 100), wx.ALL, 5)

        self.SetupPanel.SetSizer(SetupGBSizer)
        self.SetupPanel.Layout()
        ControlSizer.Add(self.SetupPanel, 0, 0, 0)

        self.ImportPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 90),
                                    wx.TAB_TRAVERSAL)
        self.ImportPanel.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.ImportPanel.SetMinSize(wx.Size(520, 90))
        self.ImportPanel.SetMaxSize(wx.Size(520, 90))

        ImpotyGBSizer = wx.GridBagSizer(0, 0)
        ImpotyGBSizer.SetFlexibleDirection(wx.BOTH)
        ImpotyGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ImpotyGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        ImpotyGBSizer.SetMinSize(wx.Size(115, 90))
        self.ImportImage = wx.StaticBitmap(self.ImportPanel, wx.ID_ANY,
                                           wx.Bitmap(u"EditIcon/Icon_Import-01.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        ImpotyGBSizer.Add(self.ImportImage, wx.GBPosition(10, 30), wx.GBSpan(10, 50), wx.ALL, 5)

        self.ImportText = wx.StaticText(self.ImportPanel, wx.ID_ANY, u"Import", wx.DefaultPosition, wx.Size(60, -1),
                                        wx.ALIGN_CENTRE)
        self.ImportText.Wrap(-1)
        self.ImportText.SetForegroundColour(wx.Colour(255, 255, 255))

        ImpotyGBSizer.Add(self.ImportText, wx.GBPosition(20, 30), wx.GBSpan(10, 50), 0, 5)

        self.ImportPanel.SetSizer(ImpotyGBSizer)
        self.ImportPanel.Layout()
        ControlSizer.Add(self.ImportPanel, 0, wx.EXPAND, 0)

        self.ActionPanel = wx.Panel(self.controlPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(520, 115),
                                    wx.TAB_TRAVERSAL)
        self.ActionPanel.SetBackgroundColour(wx.Colour(102, 102, 102))
        self.ActionPanel.SetMinSize(wx.Size(520, 115))
        self.ActionPanel.SetMaxSize(wx.Size(520, 115))

        ActionGBSizer = wx.GridBagSizer(0, 0)
        ActionGBSizer.SetFlexibleDirection(wx.BOTH)
        ActionGBSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        ActionGBSizer.SetEmptyCellSize(wx.Size(1, 1))

        ActionGBSizer.SetMinSize(wx.Size(520, 115))

        #self.ActPreviewBtn  = wx.StaticBitmap(self.ActionPanel, wx.ID_ANY,
        #                                wx.Bitmap(u"EditIcon/Icon_Preview_MouseOn-01.png", wx.BITMAP_TYPE_ANY),
        #                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.ActPreviewBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                             wx.Bitmap(u"EditIcon/Icon_Preview_MouseOn-01.png", wx.BITMAP_TYPE_ANY),
                                             wx.DefaultPosition, wx.Size(50, 50), 0)
        ActionGBSizer.Add(self.ActPreviewBtn, wx.GBPosition(20, 40), wx.GBSpan(10, 50), 0, 0)

        self.ActStartBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                           wx.Bitmap(u"EditIcon/Icon_Start_Preview-01.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.Size(60, 60), wx.BU_AUTODRAW)
        self.ActStartBtn.SetBackgroundColour( wx.Colour(128, 128, 0) )
        ActionGBSizer.Add(self.ActStartBtn, wx.GBPosition(20, 115), wx.GBSpan(10, 50), wx.EXPAND, 0)

        self.ActPauseBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                           wx.Bitmap(u"EditIcon/Icon_Pause-01.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.Size(50, 50), wx.BU_AUTODRAW)
        ActionGBSizer.Add(self.ActPauseBtn, wx.GBPosition(20, 190), wx.GBSpan(10, 50), 0, 5)

        self.ActStopBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                          wx.Bitmap(u"EditIcon/Icon_Stop-01.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(50, 50), wx.BU_AUTODRAW)
        ActionGBSizer.Add(self.ActStopBtn, wx.GBPosition(20, 270), wx.GBSpan(10, 50), 0, 5)

        self.ActExportBtn = wx.BitmapButton(self.ActionPanel, wx.ID_ANY,
                                            wx.Bitmap(u"EditIcon/Icon_Export-01.png", wx.BITMAP_TYPE_ANY),
                                            wx.DefaultPosition, wx.Size(50, 50), wx.BU_AUTODRAW)
        ActionGBSizer.Add(self.ActExportBtn, wx.GBPosition(20, 350), wx.GBSpan(10, 50), 0, 5)

        self.ActPreviewLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Preview", wx.DefaultPosition,
                                             wx.Size(50, 20), wx.ALIGN_CENTRE)
        self.ActPreviewLabel.Wrap(-1)
        self.ActPreviewLabel.SetForegroundColour(wx.Colour(255, 255, 255))

        ActionGBSizer.Add(self.ActPreviewLabel, wx.GBPosition(30, 40), wx.GBSpan(10, 50), 0, 5)

        self.ActStartLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.Size(50, 20),
                                           wx.ALIGN_CENTRE)
        self.ActStartLabel.Wrap(-1)
        self.ActStartLabel.SetForegroundColour(wx.Colour(255, 255, 255))

        ActionGBSizer.Add(self.ActStartLabel, wx.GBPosition(30, 115), wx.GBSpan(10, 50), 0, 5)

        self.ActPauseLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.Size(50, 20),
                                           wx.ALIGN_CENTRE)
        self.ActPauseLabel.Wrap(-1)
        self.ActPauseLabel.SetForegroundColour(wx.Colour(255, 255, 255))

        ActionGBSizer.Add(self.ActPauseLabel, wx.GBPosition(30, 190), wx.GBSpan(10, 50), 0, 5)

        self.ActStopLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.Size(50, 20),
                                          wx.ALIGN_CENTRE)
        self.ActStopLabel.Wrap(-1)
        self.ActStopLabel.SetForegroundColour(wx.Colour(255, 255, 255))

        ActionGBSizer.Add(self.ActStopLabel, wx.GBPosition(30, 270), wx.GBSpan(10, 50), 0, 5)

        self.ActExportLabel = wx.StaticText(self.ActionPanel, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.Size(50, 20),
                                            wx.ALIGN_CENTRE)
        self.ActExportLabel.Wrap(-1)
        self.ActExportLabel.SetForegroundColour(wx.Colour(255, 255, 255))

        ActionGBSizer.Add(self.ActExportLabel, wx.GBPosition(30, 350), wx.GBSpan(10, 50), 0, 5)

        self.blubIcon = wx.StaticBitmap(self.ActionPanel, wx.ID_ANY,
                                        wx.Bitmap(u"EditIcon/Bulb.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        ActionGBSizer.Add(self.blubIcon, wx.GBPosition(5, 450), wx.GBSpan(100, 80), 0, 5)

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

    def __del__(self):
        pass
