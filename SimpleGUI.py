import wx


class SimpleGUI(object):

    @staticmethod
    def msgbox(message, title, flags):
        try:
            app = wx.App()
            wx.MessageBox(message, title, flags)
        except Exception:
            pass


    @staticmethod
    def say(msg, title="Message"):
        __class__.msgbox(msg, title, wx.OK)

    @staticmethod
    def alert(msg, title="Alert"):
        __class__.msgbox(msg, title, wx.OK | wx.ICON_EXCLAMATION)

    @staticmethod
    def warn(msg, title="Warning"):
        __class__.msgbox(msg, title, wx.OK | wx.ICON_WARNING)

    @staticmethod
    def error(msg, title="Error"):
        __class__.msgbox(msg, title, wx.OK | wx.ICON_ERROR)

    @staticmethod
    def ask_yes_no(msg, title=""):

        yes_no = "no"

        try:
            app = wx.App()
            dialog = wx.MessageDialog(None, msg, title, wx.YES_NO | wx.ICON_QUESTION)
            result = dialog.ShowModal()
            dialog.Destroy()

            if result == wx.ID_YES:
                yes_no = "yes"
        except Exception:
            pass

        return yes_no

    @staticmethod
    def ask_text_input(message, title=""):

        value = ""

        try:
            app = wx.App()

            frame = wx.Frame(None, -1, 'win.py')
            frame.SetSize(0, 0, 200, 50)

            dlg = wx.TextEntryDialog(frame, message, title)
            result = dlg.ShowModal()
            value = dlg.GetValue()

            dlg.Destroy()
        except Exception:
            pass

        return value
