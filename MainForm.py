import clr
clr.AddReference("System.Drawing")
#
import System
from System.Windows.Forms import *
from System.Drawing import *

import SEBrowserControl as SEBC

class MainForm(Form):

    def __init__(self):
        self.Icon = Icon(".\Resources\IconApplication.ico")
        renderer = ToolStripProfessionalRenderer()
        renderer.ColorTable.UseSystemColors = True
        renderer.RoundedEdges = False
        ToolStripManager.Renderer = renderer

        # Set the application title
        self.Text = "SEBrowser in Ironpython"
        # Initialize
        self.menuStrip = MenuStrip()
        self.toolStrip = ToolStrip()
        self.sebrowser = SEBC.SEBrowserControlClass()
        self.statusStrip = StatusStrip()

        self.menuStrip.SuspendLayout()
        self.toolStrip.SuspendLayout()
        self.SuspendLayout()
        #
        # menuStrip
        #
        self.menuStrip.Dock = DockStyle.Top
        self.statusStrip.Dock = DockStyle.Bottom
        fileMenu = ToolStripMenuItem("&File")
        editMenu = ToolStripMenuItem("&Run")
        helpMenu = ToolStripMenuItem("&Help")

        ## File->Submenu
        openMenu = ToolStripMenuItem("&Open Folder...")
        openMenu.Image = Image.FromFile(".\Resources\ImageFileOpen.png")
        openMenu.ShortcutKeys = Keys.Control | Keys.O
        openMenu.Click += self.openToolStripMenuItem_Click

        exitMenu = ToolStripMenuItem("&Exit", None, self.OnExit)
        exitMenu.Image = Image.FromFile(".\Resources\IconApplication.ico")
        exitMenu.ShortcutKeys = Keys.Control | Keys.X

        fileMenu.DropDownItems.AddRange((openMenu,ToolStripSeparator(),exitMenu))
        #
        # toolStrip
        #
        openToolStripButton = System.Windows.Forms.ToolStripButton()
        runToolStripButtonSeparator = System.Windows.Forms.ToolStripButton()
        runToolStripButton = System.Windows.Forms.ToolStripButton()
        #
        # toolStrip->openToolStripButton
        #
        openToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        openToolStripButton.Image = Image.FromFile(".\Resources\ImageFileOpen.png")
        openToolStripButton.Name = "openToolStripButton"
        openToolStripButton.Size = System.Drawing.Size(23, 24)
        openToolStripButton.Text = "Open Folder (Ctrl+O)"
        openToolStripButton.Click += self.openToolStripMenuItem_Click
        #
        # toolStrip->runToolStripButtonSeparator
        #
        runToolStripButtonSeparator.Name = "runToolStripButtonSeparator"
        runToolStripButtonSeparator.Size = System.Drawing.Size(6, 27)
        #
        # toolStrip->runToolStripButton
        #
        runToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        runToolStripButton.Image = Image.FromFile(".\Resources\Run.png")
        runToolStripButton.Name = "redoToolStripButton"
        runToolStripButton.Size = System.Drawing.Size(23, 24)
        runToolStripButton.Text = "Run"
#        runToolStripButton.Click += self.runToolStripMenuItem_Click
        #
        #SEBrowserControl
        #
        self.sebrowser.AutoScroll = True
        self.sebrowser.BackColor = System.Drawing.SystemColors.Control
        self.sebrowser.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self.sebrowser.Directorypath = None
        self.sebrowser.Location = System.Drawing.Point(0, 50)
        self.sebrowser.Name = "SEBrowser"
        self.sebrowser.Size = System.Drawing.Size(860, 547)
        self.sebrowser.TabIndex = 1
        #
        # statusStrip
        #
        self.statusStrip.Text = "statusStripReady"

        # Add all together into a menu
        self.menuStrip.Items.AddRange((fileMenu,editMenu,helpMenu))

        # Add all together into a ToolMenu
        self.toolStrip.Items.AddRange((openToolStripButton, runToolStripButtonSeparator, runToolStripButton))

        #
        # MainForm
        #
        self.AutoScaleDimensions = System.Drawing.SizeF(6.0, 13.0)
        self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        self.ClientSize = System.Drawing.Size(860, 547)
        self.Controls.Add(self.statusStrip)
        self.Controls.Add(self.sebrowser)
        self.Controls.Add(self.toolStrip)
        self.Controls.Add(self.menuStrip)

        self.IsMdiContainer = True
        self.MainMenuStrip = self.menuStrip
        self.Name = "MainForm"
        # When Form loads for the first time
        self.Load += self.MainForm_Load
        self.menuStrip.ResumeLayout(False)
        self.menuStrip.PerformLayout()
        self.toolStrip.ResumeLayout(False)
        self.toolStrip.PerformLayout()
        self.ResumeLayout(False)
        self.PerformLayout()

    def MainForm_Load(self, sender, event_args):
        self.sebrowser.CreateListing()

    def openToolStripMenuItem_Click(self, sender, event_args):
        dlg = System.Windows.Forms.FolderBrowserDialog()
        if dlg.ShowDialog() == System.Windows.Forms.DialogResult.OK:
            self.Text = "SEBrowser in Ironpython"        
            self.sebrowser.Directorypath = dlg.SelectedPath
            self.Text = self.Text + " " + dlg.SelectedPath
        if self.sebrowser.Controls.Count <> 0:
            self.sebrowser.RemoveControls()
        self.sebrowser.CreateListing()

    def OnExit(self, sender, event_args):
        self.Close()