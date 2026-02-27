import os

# 성남 타겟 데이터 (동네 이름을 더 추가하고 싶으시면 리스트에 넣기만 하세요)
seongnam_data = [
    {
        "dist": "분당구",
        "towns": ["야탑동", "서현동", "이매동", "수내동", "정자동", "금곡동", "판교동", "삼평동", "백현동", "운중동", "구미동", "성남터미널", "분당", "야탑", "야탑터미널"]
    },
    {
        "dist": "수정구",
        "towns": ["복정동", "태평동", "수진동", "단대동", "산성동", "양지동", "창곡동", "신흥동"]
    },
    {
        "dist": "중원구",
        "towns": ["상대원동", "하대원동", "금광동", "은행동", "성남동", "여수동", "도촌동"]
    }
]

def generate_seongnam_pages():
    # 1. 성남시 전체 통합 페이지 생성
    reg_folder = "성남퀵서비스"
    os.makedirs(reg_folder, exist_ok=True)
    with open(f"{reg_folder}/index.html", 'w', encoding='utf-8') as f:
        f.write(f"---\nlayout: board\ntown: 성남\ntown_full: 경기도 성남시\n---")

    # 2. 각 구 및 동네별 페이지 생성
    for group in seongnam_data:
        dist_name = group['dist']
        
        # 구 페이지 생성 (예: 분당구퀵서비스)
        dist_folder = f"{dist_name}퀵서비스"
        os.makedirs(dist_folder, exist_ok=True)
        with open(f"{dist_folder}/index.html", 'w', encoding='utf-8') as f:
            f.write(f"---\nlayout: board\ntown: {dist_name}\ntown_full: 경기도 성남시 {dist_name}\n---")

        for town_name in group['towns']:
            # 동네 페이지 생성 (예: 야탑동퀵서비스)
            # 이미 구 페이지와 이름이 겹칠 일은 없으므로 단순하게 생성합니다.
            folder_name = f"{town_name}퀵서비스"
            os.makedirs(folder_name, exist_ok=True)
            
            # 내용 구성 (layout: board 유지)
            content = f"---\nlayout: board\ntown: {town_name}\ntown_full: 경기도 성남시 {dist_name} {town_name}\n---"
            
            with open(f"{folder_name}/index.html", 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✔️ 생성 완료: {folder_name}")

if __name__ == "__main__":
    generate_seongnam_pages()
    print("\n✅ 성남시 구/동별 모든 타겟 페이지 생성이 완료되었습니다.")
