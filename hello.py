from flask import Flask, render_template_string, request
import os
import psycopg2

app = Flask(_name_)

DATABASE_URL = os.getenv("DATABASE_URL", "")
HTML ="""
<! doctype html>
<html>
<head>
 <title>Buluttan Selam !< /title>
 <style>
  body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
  h1 { color: #333; }
  form { margin: 20px auto; }
  input { padding: 10px; font-size: 16px; }
  button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; }
  ul { list-style: none; padding: 0; }
  li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
</style>
