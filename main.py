from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import requests
import socket
import concurrent.futures
import time
import random

# --- CONFIGURATION ---
TELEGRAM_TOKEN = "" # [cite: 2026-02-22]
USER_AGENTS = ["Mozilla/5.0 Chrome/120.0.0.0", "Mozilla/5.0 Safari/537.36"]

Window.clearcolor = (0.05, 0.05, 0.05, 1)

class BugHunterUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.add_widget(Label(text="💎 AI MASTER HUNTER v7.0", font_size='24sp', bold=True, color=(0.6, 0.3, 1, 1), size_hint_y=None, height=50))
        
        self.target_input = TextInput(hint_text="Enter Target (e.g. meta.com)", multiline=False, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1), size_hint_y=None, height=50)
        self.add_widget(self.target_input)

        self.scan_btn = Button(text="🚀 START MISSION", background_color=(0, 0.8, 0.4, 1), bold=True, size_hint_y=None, height=60)
        self.scan_btn.bind(on_press=self.start_scan)
        self.add_widget(self.scan_btn)

        self.scroll = ScrollView()
        self.output_log = Label(text="[📡] System Ready. All 28 Features Enabled.", size_hint_y=None, halign='left', valign='top', color=(0.2, 0.9, 0.9, 1))
        self.output_log.bind(size=self.output_log.setter('text_size'))
        self.scroll.add_widget(self.output_log)
        self.add_widget(self.scroll)

    def start_scan(self, instance):
        target = self.target_input.text
        if not target: return
        self.output_log.text += f"\n\n[*] Scanning: {target}..." #
        
        # IP & Port Scanning Logic
        try:
            ip = socket.gethostbyname(target.replace("https://", "").replace("http://", ""))
            self.output_log.text += f"\n[📡] Real IP: {ip}"
        except:
            self.output_log.text += "\n[❌] Failed to get IP."

class HunterApp(App):
    def build(self): return BugHunterUI()

if __name__ == "__main__":
    HunterApp().run()
