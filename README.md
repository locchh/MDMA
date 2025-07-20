# MDMA

Mood-Driven Music Agents

## Design

### Roles

**User**: The user of the system.

**Chat Agent**:
- Talk to user.
- Approve the music suggestions of **Music Selector Agent**.
- Only the **Chat Agent** can send the message to the user.

**Mood Detector Agent**:
- Detect user's mood base on the conversation of **Chat Agent** and **User**.
- If the mood is not clear, send the question to **Chat Agent** to ask the user for clarification.
- If the mood is clear, send the mood to **Music Selector Agent**.

**Music Selector Agent**:
- Select music based on the mood received from **Mood Detector Agent**.
- Suggest music to **Chat Agent** and explain why the music is suggested.


## Reference

- [Autogen](https://microsoft.github.io/autogen/stable/index.html)
