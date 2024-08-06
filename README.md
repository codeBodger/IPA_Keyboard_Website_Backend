# IPA Keyboard Website Backend
This Backend, written in Python, is really just a way for the [Website](https://github.com/codeBodger/IPA_Keyboard_Website?tab=readme-ov-file#readme) to communicate with the [Router Server](https://github.com/codeBodger/IPA_Keyboard_Router_Server?tab=readme-ov-file#readme). 

To make this work with Apache, it had to be almost entirely rewritten, as Apache is already running the server, so there is instead a Python script that is POSTed to. 

This Backend is really quite simple.  It just takes the data it gets from POST from the [Website](https://github.com/codeBodger/IPA_Keyboard_Website?tab=readme-ov-file#readme) and sends it to the [Router Server](https://github.com/codeBodger/IPA_Keyboard_Router_Server?tab=readme-ov-file#readme), prepended with a single byte indicating the activity.  When the activity is to send which character to type, it converts the key-code to the key-byte first. 

This Backend also handles passing response codes from the [Router Server](https://github.com/codeBodger/IPA_Keyboard_Router_Server?tab=readme-ov-file#readme) to the [Website](https://github.com/codeBodger/IPA_Keyboard_Website?tab=readme-ov-file#readme).  These are used to ensure that everything is working properly and to alert the user if something went wrong, so they can either resolve the problem or contact me about it.  

## Definitions
|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| Key‑code:     | the three digit<sub>10</sub> (000-164) code representing a single IPA character        |
| Key‑byte:     | the key-code as a single byte (typically implicitly casted to `int`)                   |
| Long‑code:    | the 18 digit<sub>64</sub> code to indicate which client a key-byte needs to be sent to |
| Linking‑code: | the six digit<sub>10</sub> code to get the long-code from Router Server to Website     |
