import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

def notify(text:str):
    #create notifier
    nManager = notifications.ToastNotificationManager
    notifier = nManager.create_toast_notifier()

    #define your notification as string
    tString = f"""
    <toast>
        <visual>
            <binding template='ToastGeneric'>
                <text>Степан</text>
                <text>{text}</text>
            </binding>
        </visual>
    </toast>
    """

    #convert notification to an XmlDocument
    xDoc = dom.XmlDocument()
    xDoc.load_xml(tString)

    #display notification
    notifier.show(notifications.ToastNotification(xDoc))