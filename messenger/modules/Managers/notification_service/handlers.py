from messenger.modules.Managers.notification_service.notification_manager import NotificationManager

notification_manager = NotificationManager()

@notification_manager.notify("/email")
async def send_email_notification(data: dict):
    print("send email")