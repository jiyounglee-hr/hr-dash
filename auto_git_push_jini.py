import os
import subprocess
from datetime import datetime
import hashlib

# 경로 설정
EXCEL_FILE = r"C:\Users\neurophet1\OneDrive - 뉴로핏 주식회사\☆인사\05. 임직원\000. 임직원 명부\통계자동화\임직원 기초 데이터.xlsx"
REPO_DIR = r"C:\Users\neurophet1\OneDrive - 뉴로핏 주식회사\☆인사\05. 임직원\000. 임직원 명부\통계자동화"
HASH_FILE = os.path.join(REPO_DIR, "last_hash.txt")  # 파일 변경 추적용

def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def main():
    with open(os.path.join(REPO_DIR, "auto_push_log.txt"), "a") as log:
        log.write(f"{datetime.now()} - 실행 시작\n")

    os.chdir(REPO_DIR)
    current_hash = get_file_hash(EXCEL_FILE)

    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            last_hash = f.read()
        if current_hash == last_hash:
            print("변경 없음.")
            return

    # 모든 변경사항을 스테이징
    subprocess.run(["git", "add", "."], check=True)
    
    # 원격 저장소의 변경사항을 가져옴
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError:
        print("pull 중 오류 발생, 계속 진행합니다.")
    
    commit_msg = f"자동 커밋: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push"], check=True)
    print("변경 감지 → GitHub에 푸시 완료.")

    with open(HASH_FILE, "w") as f:
        f.write(current_hash)

if __name__ == "__main__":
    main()