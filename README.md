# Tikrar System — Tahfeez Registration Web App

A mobile-friendly Streamlit adaptation of the supplied `Tikrar sys.py` terminal registration programme.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in the terminal. Streamlit's network URL can be opened by a phone on the same Wi-Fi network.

## Deploy and get a public shareable link

1. Create or sign in to a GitHub account.
2. Create a new repository, for example `tikrar-system`.
3. Upload `app.py` and `requirements.txt` to the repository.
4. Open [Streamlit Community Cloud](https://share.streamlit.io/).
5. Connect GitHub and choose the repository, branch, and `app.py` as the main file.
6. Deploy. Streamlit will provide a public `*.streamlit.app` link that can be shared with Android users.

## Updating the application

Edit `app.py` in the GitHub repository and commit the changes. Streamlit Community Cloud normally redeploys the app from the updated repository.

## Important current limitations

- The supplied source ends after printing the programme pillars. This version therefore implements only the registration flow present in that source.
- The source does not define a database, admin dashboard, email/SMS delivery, or permanent registration storage. The current version keeps answers in the active Streamlit session and displays a review screen; it does not permanently save or submit registrations.
- The original `input()`/`print()` interface is represented as one typed web prompt per step. The order, accepted values, and validation intent are retained, but terminal loops are adapted to Streamlit session state.
  
- The supplied code's motto spelling was polished from "Nuturing" to "Nurturing" in the interface. The programme identity and pillars are retained.

## Security and privacy before public launch

The current form collects personal information, including phone numbers and residential addresses. Before using it with real students, add an appropriate secure database, access controls, a privacy notice, retention rules, and a process for handling guardian consent where applicable. Do not treat the current session preview as a permanent registration system.
