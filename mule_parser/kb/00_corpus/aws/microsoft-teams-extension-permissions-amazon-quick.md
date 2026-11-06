# Microsoft Teams extension permissions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/teams-extension-permissions.html](https://docs.aws.amazon.com/quick/latest/userguide/teams-extension-permissions.html)

---

The Amazon Quick Microsoft Teams extension uses Microsoft's Resource-Specific Consent (RSC) framework. The bot only gets access to the specific meetings and chats where it is installed — not tenant-wide access to all Teams data. These permissions are granted automatically when the app is added to a meeting or chat; no additional admin action is needed.

The following table lists the RSC permissions used by the Teams extension.

| Permission | Purpose | Feature | 
|---|---|---|
| `ChatMessage.Read.Chat` | Read chat messages for AI assistant context | General chat assistant | 
| `ChatMember.Read.Chat` | Resolve attendee emails and identify the meeting organizer for summary delivery | Meeting Summary | 
| `OnlineMeeting.ReadBasic.Chat` | Read meeting name, schedule, and organizer info | Meeting Summary | 
| `OnlineMeetingTranscript.Read.Chat` | Retrieve transcripts after a meeting ends | Meeting Summary | 
| `OnlineMeetingParticipant.Read.Chat` | Read participant join/leave times and roles | Meeting Summary | 
| `ChannelMessage.Read.Group` | Read thread context when the bot is @mentioned in a channel | General chat assistant | 
| `ChannelMeeting.ReadBasic.Group` | Read basic properties of channel meetings | Meeting Summary | 
| `ChannelMeetingTranscript.Read.Group` | Retrieve transcripts of channel meetings | Meeting Summary | 
| `ChannelMeetingParticipant.Read.Group` | Read participant info for channel meetings | Meeting Summary | 

## Installation permission (revoke after install)

                The following permission is automatically granted during app installation and must be revoked afterward. It is not required for ongoing operation.

| Permission | Purpose | Required admin action | 
|---|---|---|
| `AppCatalog.ReadWrite.All` | Read and write to all app catalogs (used during installation only) | Revoke after installation via Microsoft Entra
                                    > Enterprise Applications>Permissions | 

###### Important

After installation, go to Microsoft Entra >
                            **Enterprise Applications**, find the app starting with
                        "qbs" and ending with "teams", navigate to
                            **Permissions**, and revoke
                            `AppCatalog.ReadWrite.All`.

## Where to review permissions

                Use the following locations to review permissions for the Microsoft Teams extension:

- 
                        **RSC Permissions:**Teams Admin Center >**Teams apps**>**Manage apps**>**Amazon Quick**>**Permissions**
- 
                        **Application Permissions:**Microsoft Entra >**Enterprise Applications**> find the app starting with "qbs" and ending with "teams" >**Permissions**