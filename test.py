import csv
import os
#w+ - 읽기 쓰기, 파일이 없으면 새로 만듬
#w - 쓰기 모드, 파일이 없으면 새로 만듬
#r+ 읽기 쓰기, 파일이 없으면 에러
#r - 읽기 모드, 파일이 없으면 에러
#a+ 읽기 쓰기, 파일이 없으면 새로만듬
#a - 파일 추가 모드 , 파일이 없으면 새로만듬

# f = open("test.csv", "a+", encoding='utf-8', newline="")
# csv_w = csv.writer(f)
# csv_w.writerow(["이름","이메일","전화번호"])
# f.close()

f2 = open("test.csv","r",encoding="utf-8")
csv_r = csv.reader(f2)
for line in csv_r:
    print(line[2])
f2.close()

os.getenv("NAVER_ID")
os.getenv("NAVER_SECRET")
os.getenv("KOBIS_KEY")
# echo 'export KOBIS_KEY="3f3ac1621d7ac6f0efbeb7a1e012b718"' >> ~/.bashrc
# echo 'export NAVER_ID="HUuSEm7B0grrk3PO59sz"' >> ~/.bashrc
# echo 'export NAVER_SECRET="WM5o_wVWyF"' >> ~/.bashrc