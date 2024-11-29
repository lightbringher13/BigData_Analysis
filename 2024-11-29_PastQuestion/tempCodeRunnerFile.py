# 두 독립 집단 간 순위 분포 차이를 검정 (정규성 가정 없음).
# 두 그룹의 반응 시간이 동일한 분포인지 검정.
group_a = [5.1, 5.3, 5.2, 5.5, 5.6]
group_b = [5.7, 5.8, 5.9, 6.0, 6.1]
u_stat, p_value = mannwhitneyu(group_a, group_b)
if p_value < 0.05:
    print("귀무가설 기각: 두 그룹 간 분포에 차이가 있습니다.")
else:
    print("귀무가설 채택: 두 그룹 간 분포에 차이가 없습니다.")