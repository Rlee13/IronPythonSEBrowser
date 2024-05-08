import clr, os
clr.AddReference("System.Drawing")
#
import System
from System.Windows.Forms import *
from System.Drawing import *

import SEBrowserControl as SEBC

class MainForm(Form):

    def __init__(self):
        self.Icon = Icon(".\Resources\IconApplication.ico")

        # Set the application title
        self.Text = "SEBrowser"
        # Initialize
        self.menuStrip = MenuStrip()
        self.toolStrip = ToolStrip()
        self.sebrowser = SEBC.SEBrowserControlClass()
        self.statusStrip = StatusStrip()

        #
        # menuStrip
        #
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
        runToolStripButtonSeparator.Size = System.Drawing.Size(6, 24)
        #
        # toolStrip->runToolStripButton
        #
        runToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        runToolStripButton.Image = Image.FromFile(".\Resources\Run.png")
        runToolStripButton.Name = "runToolStripButton"
        runToolStripButton.Size = System.Drawing.Size(23, 24)
        runToolStripButton.Text = "Run"
#        runToolStripButton.Click += self.runToolStripMenuItem_Click
        #
        #SplitContainer
        #
        self.SplitContainer1 = System.Windows.Forms.SplitContainer()
        self.TreeView1 = System.Windows.Forms.TreeView()
        #
        #SplitContainer1
        #
        self.SplitContainer1.Dock = System.Windows.Forms.DockStyle.Fill
        self.SplitContainer1.Location = System.Drawing.Point(0, 24)
        self.SplitContainer1.Name = "SplitContainer1"
        #
        #SplitContainer1.Panel1
        #
        self.SplitContainer1.Panel1.Controls.Add(self.TreeView1)
        #
        #SplitContainer1.Panel2
        #
        self.SplitContainer1.Panel2.Controls.Add(self.sebrowser)
        self.SplitContainer1.Panel2.AutoScroll = True
        self.SplitContainer1.Size = System.Drawing.Size(860, 500)
        self.SplitContainer1.SplitterDistance = 260
        #
        #TreeView1
        #
        self.TreeView1.Dock = System.Windows.Forms.DockStyle.Fill
        self.TreeView1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.TreeView1.Location = System.Drawing.Point(0, 0)
        self.TreeView1.Name = "TreeView1"
        self.TreeView1.Size = System.Drawing.Size(260, 500)
        self.TreeView1.TabIndex = 0
        self.TreeView1.BeforeExpand += self.TreeView1_BeforeExpand
        self.TreeView1.AfterSelect += self.TreeView1_AfterSelect
        #
        #SEBrowserControl
        #
        self.sebrowser.Dock = System.Windows.Forms.DockStyle.Fill
        self.sebrowser.AutoScroll = True
        self.sebrowser.BackColor = System.Drawing.SystemColors.Control
        self.sebrowser.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        # self.sebrowser.Directorypath = None
        # self.sebrowser.Location = System.Drawing.Point(0, 50)
        self.sebrowser.Name = "SEBrowser"
        self.sebrowser.Size = System.Drawing.Size(600, 500)
        self.sebrowser.TabIndex = 1
        #
        # statusStrip
        #
        self.toolStripStatusLabel = System.Windows.Forms.ToolStripStatusLabel()
        self.statusStrip.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem]([self.toolStripStatusLabel]))
        self.statusStrip.Location = System.Drawing.Point(0, 500)
        self.statusStrip.Name = "statusStrip"
        self.statusStrip.Size = System.Drawing.Size(860, 50)
        #
        # toolStripStatusLabel
        #
        self.toolStripStatusLabel.Name = "toolStripStatusLabel"
        self.toolStripStatusLabel.Size = System.Drawing.Size(120, 50)
        self.toolStripStatusLabel.Text = "statusStripReady"

        # Add all together into a menu
        self.menuStrip.Items.AddRange((fileMenu,editMenu,helpMenu))

        # Add all together into a ToolMenu
        self.toolStrip.Items.AddRange((openToolStripButton, runToolStripButtonSeparator, runToolStripButton))

        #
        # MainForm
        #
        self.AutoScaleDimensions = System.Drawing.SizeF(6.0, 13.0)
        self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        self.ClientSize = System.Drawing.Size(860, 550)
        self.Controls.Add(self.SplitContainer1)
        self.Controls.Add(self.statusStrip)
        # self.Controls.Add(self.sebrowser)
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
        # getInfo = System.IO.DriveInfo.GetDrives()
        # for info in getInfo:
        #     print (info)

#        initFolder = "C:\\"
        initFolder = os.getcwd() + "/Resources"
        rootnode = self.TreeView1.Nodes.Add(initFolder)
        self.FillChildNodes(rootnode)
        self.TreeView1.Nodes[0].Expand()

    def FillChildNodes(self, node):
        try:
            dirs = System.IO.DirectoryInfo(node.FullPath)
#            print dirs
            for dirInfo in dirs.GetDirectories():
                try:
                    newnode = System.Windows.Forms.TreeNode(dirInfo.Name)
                    node.Nodes.Add(newnode)
                    if [name for name in os.listdir(newnode.FullPath) if os.path.isdir(os.path.join(newnode.FullPath, name))] != []:
                        newnode.Nodes.Add("*")
                except Exception as ex:
                    newnode.ForeColor = System.Drawing.Color.Gray
                    print (ex)
                    continue

        except Exception as ex:
            print (ex)
            pass

    def TreeView1_BeforeExpand(self, sender, e):
#        print "treeView1_BeforeExpand"
        if (e.Node.Nodes[0].Text == "*"):
            e.Node.Nodes.Clear()
            self.FillChildNodes(e.Node)

    def TreeView1_AfterSelect(self, sender, event_args):
#        print "TreeView1_AfterSelect"
        self.Text = "SEBrowser: "
        pathName = self.TreeView1.SelectedNode.FullPath
        self.sebrowser.Directorypath = pathName
        self.Text = self.Text + " " + pathName
        if self.sebrowser.Controls.Count != 0:
            self.sebrowser.RemoveControls()        
        self.sebrowser.CreateListing()

    def openToolStripMenuItem_Click(self, sender, event_args):
        dlg = System.Windows.Forms.FolderBrowserDialog()
        if dlg.ShowDialog() == System.Windows.Forms.DialogResult.OK:
            self.Text = "SEBrowser"        
            self.sebrowser.Directorypath = dlg.SelectedPath
            self.Text = self.Text + " " + dlg.SelectedPath
        if self.sebrowser.Controls.Count != 0:
            self.sebrowser.RemoveControls()
        self.sebrowser.CreateListing()

    def OnExit(self, sender, event_args):
        self.Close()