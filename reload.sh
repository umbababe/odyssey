#!/bin/bash

REPO_DIR="/home/luha/project"
STREAMLIT_CMD="streamlit run app.py"

# GitHub 저장소 업데이트
cd $REPO_DIR
git pull origin main

# 기존 Streamlit 서버 중지
pkill -f "streamlit run"

# Streamlit 서버 재시작
$STREAMLIT_CMD &

