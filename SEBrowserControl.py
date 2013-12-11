import clr
clr.AddReference("System.Drawing")
clr.AddReference("Interop.SeThumbnailLib.dll")
#
import System
import os
import SeThumbnailLib as SETL

class SEBrowserControlClass(System.Windows.Forms.UserControl):
    def __init__(self):
        self.AutoScaleDimensions = System.Drawing.SizeF(6.0, 13.0)
        self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        self.AutoScroll = True
        self.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self.Name = "SEBrowser"
        self.Dock = System.Windows.Forms.DockStyle.Fill
        self.ResumeLayout(False)
        
        self.Directorypath = ""

    def CreateListing(self):
        self.XLocation = 25
        self.YLocation = 25
        self.PicWidth = 130
        self.PicHeight = 120
        self.SuspendLayout()
        if self.Directorypath is not None:
            diar = []
            for filename in os.listdir(self.Directorypath):
                if filename.endswith(".par") or filename.endswith(".asm"):
                    diar.append(filename)
            for dra in diar:
                self.DrawGroupBox(dra)

        self.ResumeLayout()

    def DrawGroupBox(self, filename):
        self.GroupBox1 = System.Windows.Forms.Label()
        self.Label1 = System.Windows.Forms.Label()
        self.PictureBox1 = System.Windows.Forms.PictureBox()

        self.GroupBox1.Location = System.Drawing.Point(self.XLocation, self.YLocation)
        self.XLocation = self.XLocation + self.PicWidth + 20
        if self.XLocation + self.PicWidth >= self.Width:
            self.XLocation = 25
            self.YLocation = self.YLocation + self.PicHeight + 20

        self.GroupBox1.Name = filename
        self.GroupBox1.Size = System.Drawing.Size(self.PicWidth, self.PicHeight)
        self.GroupBox1.TabIndex = 0
        self.GroupBox1.TabStop = False
        self.GroupBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle

        self.PictureBox1.Location = System.Drawing.Point(0, 0)
        self.PictureBox1.Size = System.Drawing.Size(self.PicWidth, self.PicHeight-20)
        self.Label1.Location = System.Drawing.Point(0, self.PicHeight-15)
        self.Label1.Size = System.Drawing.Size(self.PicWidth, 15)
        self.Label1.Text = filename
        self.Label1.TextAlign = System.Drawing.ContentAlignment.TopCenter

        thumbnailExtractor = SETL.SeThumbnailExtractorClass()
        hBitmap = None
        fullpath = self.Directorypath + "\\" + filename

        hBitmap = thumbnailExtractor.GetThumbnail(fullpath, hBitmap)
        if (hBitmap <> System.IntPtr.Zero):
            self.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
            self.PictureBox1.WaitOnLoad = True
            self.PictureBox1.Image = System.Drawing.Image.FromHbitmap(System.IntPtr(hBitmap))
        
        self.GroupBox1.Controls.Add(self.PictureBox1)
        self.GroupBox1.Controls.Add(self.Label1)
        self.Controls.Add(self.GroupBox1)

    def RemoveControls(self):
        for ctrl in reversed(self.Controls):
            for inctrl in reversed(ctrl.Controls):
                ctrl.Controls.Remove(inctrl)
                inctrl.Dispose()
            self.Controls.Remove(ctrl)
            ctrl.Dispose()
