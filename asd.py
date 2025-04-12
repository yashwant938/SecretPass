import streamlit as st
from Crypto.Cipher import DES
from base64 import b64encode, b64decode
from datetime import datetime
KEY = b'8bytekey'  
# UserName="TheHack?"
PASSWORD = "Lmaquvg@2005ghT#163783@oeje"

def pad(text):
    """Pads text to be a multiple of 8 bytes"""
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_des(text):
    cipher = DES.new(KEY, DES.MODE_ECB)
    padded_text = pad(text)
    encrypted = cipher.encrypt(padded_text.encode('utf-8'))
    return b64encode(encrypted).decode('utf-8')

def decrypt_des(encrypted_text):
    cipher = DES.new(KEY, DES.MODE_ECB)
    decrypted = cipher.decrypt(b64decode(encrypted_text)).decode('utf-8')
    return decrypted.strip()

encrypted_password = encrypt_des(PASSWORD)

st.title("🔒 Secure DES Decryption App")

st.write("**Encrypted Password:**")
st.code(encrypted_password, language='text')

st.markdown("---")
now = datetime.now()
is_weekend = now.weekday() in [5, 6]  # 5 = Saturday, 6 = Sunday
is_valid_time = now.hour == 23  # 11 PM

if st.button("🔓 Decrypt"):
    if is_weekend and is_valid_time:
        decrypted = decrypt_des(encrypted_password)
        st.success(f"Decrypted Password: {decrypted}")
    else:
        st.warning("Yash, You can do it! Never give up on your dream. You have a lot of things to do — don't waste time! 💪🚀")


