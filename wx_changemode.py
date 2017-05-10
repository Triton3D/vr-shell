import wx
CurrDisplay=wx.Display
OldMode=wx.DefaultVideoMode
ListVideoModes=CurrDisplay.GetModes(CurrDisplay())
NewMode=ListVideoModes[len(ListVideoModes)-35]
MaxWidth=NewMode.GetWidth()
MaxHeight=NewMode.GetHeight()
print(str(MaxWidth)+'x'+str(MaxHeight))
CurrDisplay.ChangeMode(CurrDisplay(),NewMode)
input("HI")
    
    
