from scipy.stats import pearsonr
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency
import numpy as np
from scipy.stats import chisquare
from scipy.stats import f_oneway
import scipy.stats
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import mannwhitneyu

# 가설 검정

# 한 집단의 평균이 특정 값과 다른지 확인
# 학생들의 평균 시험 점수가 70점과 다른지 확인.
scores = [68, 72, 71, 69, 70, 73]
mean = 70
t_stat, p_value = ttest_1samp(scores, mean)
print(p_value)
if p_value < 0.05:
    print("귀무가설 기각: 평균이 같다.")
else:
    print("귀무가설 채택")

# ttest_ind 두 독립된 집단의 평균 차이를 검정
# 남학생과 여학생의 평균 키에 차이가 있는지 확인
male_heights = [170, 175, 168, 180, 178]
female_heights = [160, 162, 165, 161, 159]
t_stat, p_value = ttest_ind(male_heights, female_heights)
if p_value < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 채택")

# 동일 집단에서 전/후 상태의 평균차이를 검정
# 다이어트 전과 후 체중 차이를 점검
before_diet = [72, 75, 80, 85, 90]
after_diet = [70, 73, 77, 83, 88]
t_stat, p_value = ttest_rel(before_diet, after_diet)
if p_value < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 채택")

# 세 개 이상의 집단 간 평균 차이를 검정
# 지역 A,B,C의 평균 판매량에 차이가 있는지 검정
region_a = [200, 210, 190, 220, 230]
region_b = [180, 190, 200, 210, 195]
region_c = [250, 240, 245, 255, 260]
f_stat, p_value = f_oneway(region_a, region_b, region_c)
if p_value < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 채택")

# 관측 빈도가 기대 빈도와 일치하는지 검정
# 주사위가 공정하게 작동하는지 확인
observed = [16, 18, 16, 14, 12, 14]  # 관측된 주사위 값
expected = [15, 15, 15, 15, 15, 15]  # 기대되는 주사위 값
chi2, p_value = chisquare(observed, expected)
if p_value < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 채택")

# 두 범주형 변수 간 독립 여부를 검정
# 남성과 여성 간 흡연 여부에 차이가 있는지 검정
data = np.array([
    [120, 480],
    [143, 407]
])
chi2, p_value, dof, expected = chi2_contingency(data)
print(chi2)
print(p_value)
print(dof)
print(expected)
if p_value < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 채택")


# 두 독립 집단 간 순위 분포 차이를 검정 (정규성 가정 없음).
# 두 그룹의 반응 시간이 동일한 분포인지 검정.
group_a = [5.1, 5.3, 5.2, 5.5, 5.6]
group_b = [5.7, 5.8, 5.9, 6.0, 6.1]
u_stat, p_value = mannwhitneyu(group_a, group_b)
if p_value < 0.05:
    print("귀무가설 기각: 두 그룹 간 분포에 차이가 있습니다.")
else:
    print("귀무가설 채택: 두 그룹 간 분포에 차이가 없습니다.")


# 두 연속형 변수 간 선형 상관관계 검정.
# 키와 체중 간 상관관계 확인.
height = [150, 160, 170, 180, 190]
weight = [50, 60, 70, 80, 90]
correlation, p_value = pearsonr(height, weight)
print(correlation)
if p_value < 0.05:
    print("귀무가설 기각: 키와 체중 간 상관관계가 있습니다.")
else:
    print("귀무가설 채택: 키와 체중 간 상관관계가 없습니다.")

# 분석회귀 모델
