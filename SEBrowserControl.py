import clr, sys, os
sys.path.append(os.getcwd() + "/Libs")

clr.AddReference("System.Drawing")
clr.AddReference("Interop.SeThumbnailLib.dll")
#
import System
import SeThumbnailLib as SETL

class SEBrowserControlClass(System.Windows.Forms.UserControl):
    def __init__(self):
        self.AutoScaleDimensions = System.Drawing.SizeF(6.0, 13.0)
        self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        self.AutoScroll = True
        self.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self.Name = "SEBrowser"
        self.Dock = System.Windows.Forms.DockStyle.Fill
        self._tabindex = 1

        self.ResumeLayout(False)
        
        self.Directorypath = os.getcwd() + "/Resources"

    def CreateListing(self):
        self.XLocation = 25
        self.YLocation = 5
        self.PicWidth = 120
        self.PicHeight = 120
        self.SuspendLayout()
        if self.Directorypath is not None:
            diar = []
            for filename in os.listdir(self.Directorypath):
                if filename.endswith((".par", ".asm")):
                    diar.append(filename)
            for dra in diar:
                self.DrawGroupBox(dra)

        self.ResumeLayout()

    def DrawGroupBox(self, filename):

        thumbnailExtractor = SETL.SeThumbnailExtractorClass()
        hBitmap = None
        fullpath = self.Directorypath + "\\" + filename

        hBitmap = thumbnailExtractor.GetThumbnail(fullpath, hBitmap)
        # if (hBitmap != System.IntPtr.Zero):
        if (hBitmap != 0):
            self.GroupBox1 = System.Windows.Forms.Panel()
            self.Label1 = System.Windows.Forms.Label()
            self.PictureBox1 = System.Windows.Forms.PictureBox()

            self.GroupBox1.Location = System.Drawing.Point(self.XLocation, self.YLocation)
            self.XLocation = self.XLocation + self.PicWidth + 20
            if self.XLocation + self.PicWidth >= self.Width:
                self.XLocation = 25
                self.YLocation = self.YLocation + self.PicHeight + 20

            self.PictureBox1.Location = System.Drawing.Point(0, 0)
            self.PictureBox1.Size = System.Drawing.Size(self.PicWidth, self.PicHeight-20)
            self.PictureBox1.Click += self.GB_Click

            self.Label1.Location = System.Drawing.Point(0, self.PicHeight-15)
            self.Label1.Size = System.Drawing.Size(self.PicWidth, 15)
            self.Label1.Text = filename
            self.Label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
            self.Label1.Click += self.GB_Click

            self.GroupBox1.Name = filename
            self.GroupBox1.Size = System.Drawing.Size(self.PicWidth, self.PicHeight)
            self.PictureBox1.TabIndex = self._tabindex
            self._tabindex += 1
            # self.GroupBox1.BorderStyle = None
            # self.GroupBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
            self.GroupBox1.Click += self.GB_Click

            self.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
            self.PictureBox1.WaitOnLoad = True
            self.PictureBox1.Image = System.Drawing.Image.FromHbitmap(System.IntPtr(hBitmap))
        
            self.GroupBox1.Controls.Add(self.PictureBox1)
            self.GroupBox1.Controls.Add(self.Label1)
            self.Controls.Add(self.GroupBox1)

    def RemoveControls(self):
        self.Controls.Clear()

    def GB_Click(self, sender, event_args):
        if type(sender) == type(self.PictureBox1) or type(sender) == type(self.Label1):
            GB = sender.Parent
        if type(sender) == type(self.GroupBox1):
            GB = sender

        # for ctrl in self.Controls:
            # ctrl.BorderStyle = None
            # ctrl.BorderStyle = System.Windows.Forms.BorderStyle.None

        GB.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        _spliterpanel = self.Parent
        _splitcontainer = _spliterpanel.Parent
        _splitcontainer.Parent.toolStripStatusLabel.Text = str(GB.Name)