import streamlit as st
import hashlib
import json
import os
from datetime import datetime

class Authentication:
    def __init__(self):
        self.users_file = "users.json"
        self.load_users()
    
    def load_users(self):
        """Load users from JSON file"""
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}
    
    def save_users(self):
        """Save users to JSON file"""
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, password, email):
        """Register a new user"""
        if username in self.users:
            return False, "Username already exists"
        
        self.users[username] = {
            "password": self.hash_password(password),
            "email": email,
            "created_at": datetime.now().isoformat(),
            "last_login": None
        }
        self.save_users()
        return True, "User registered successfully"
    
    def authenticate_user(self, username, password):
        """Authenticate user credentials"""
        if username not in self.users:
            return False, "Username not found"
        
        if self.users[username]["password"] == self.hash_password(password):
            self.users[username]["last_login"] = datetime.now().isoformat()
            self.save_users()
            return True, "Login successful"
        
        return False, "Invalid password"
    
    def show_auth_page(self):
        """Display authentication page with glassmorphism design"""
        
        # Custom CSS for auth page
        st.markdown("""
        <style>
        .auth-container {
            background: linear-gradient(135deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .auth-card {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        
        .auth-title {
            color: #2d3436;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .auth-subtitle {
            color: #636e72;
            font-size: 1.1rem;
            margin-bottom: 30px;
        }
        
        .stTextInput > div > div > input {
            background: rgba(255, 255, 255, 0.3);
            border: 1px solid rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            color: #2d3436;
            backdrop-filter: blur(10px);
        }
        
        .stTextInput > div > div > input::placeholder {
            color: rgba(0, 0, 0, 0.6);
        }
        
        .stButton > button {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 2px solid #2c3e50 !important;
            border-radius: 25px !important;
            color: #2c3e50 !important;
            font-weight: bold !important;
            padding: 0.5rem 2rem !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
        }
        
        .stButton > button:hover {
            background: rgba(255, 255, 255, 1) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 5px 15px rgba(44, 62, 80, 0.3) !important;
        }
        
        /* Enhanced Gradient text with green+blue combination */
        .gradient-text {
            background: linear-gradient(90deg, #16a085 0%, #2ecc71 25%, #3498db 75%, #2980b9 100%);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            animation: gradient 3s ease infinite;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Enhanced gradient text for titles */
        .gradient-title {
            background: linear-gradient(90deg, #16a085 0%, #2ecc71 25%, #3498db 75%, #2980b9 100%);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            font-weight: 900;
            font-size: 2.5rem;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
            filter: drop-shadow(2px 2px 8px rgba(0,0,0,0.4));
            animation: gradient 4s ease infinite;
            letter-spacing: -0.02em;
            line-height: 1.1;
        }
        
        /* Gradient text for labels and smaller text */
        .gradient-label {
            background: linear-gradient(135deg, #27ae60, #3498db);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            font-weight: 600;
            filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.2));
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Center the authentication form
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            
            # Title
            st.markdown('<h1><span class="emoji-normal">📈</span> <span class="gradient-title">Stock Dashboard</span></h1>', unsafe_allow_html=True)
            st.markdown('<p class="gradient-label">Real-time Indian Stock Market Analytics</p>', unsafe_allow_html=True)
            
            # Login/Register tabs
            tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
            
            with tab1:
                self.show_login_form()
            
            with tab2:
                self.show_register_form()
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    def show_login_form(self):
        """Display login form"""
        with st.form("login_form"):
            st.markdown("### Sign In")
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            if st.form_submit_button("🚀 Login", use_container_width=True):
                if username and password:
                    success, message = self.authenticate_user(username, password)
                    if success:
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please fill in all fields")
    
    def show_register_form(self):
        """Display registration form"""
        with st.form("register_form"):
            st.markdown("### Create Account")
            new_username = st.text_input("Username", placeholder="Choose a username")
            new_email = st.text_input("Email", placeholder="Enter your email")
            new_password = st.text_input("Password", type="password", placeholder="Create a password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            
            if st.form_submit_button("✨ Register", use_container_width=True):
                if new_username and new_email and new_password and confirm_password:
                    if new_password == confirm_password:
                        if len(new_password) >= 6:
                            success, message = self.register_user(new_username, new_password, new_email)
                            if success:
                                st.success(message)
                                st.info("Please switch to the Login tab to sign in")
                            else:
                                st.error(message)
                        else:
                            st.error("Password must be at least 6 characters long")
                    else:
                        st.error("Passwords do not match")
                else:
                    st.warning("Please fill in all fields")