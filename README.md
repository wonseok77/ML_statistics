# kdigital_ML_statistic
### 내재화
### 머신러닝
- 1day
    - 01_도미와_빙어_구분하기
     - KNN 성능개선점 : k근접이웃 개수 설정 파라미터 : n_neighbors = 5 
     - 리스트 병합 : 그냥 + 쓰면된다 , 반복데이터 만들기 [1] * 35 +  [0] * 14
     - 이차원형태로 만들기 : 1. for문 이용, 2. 리스트컴프리헨션 + zip 함수, 3. np.column_stack((a,b))

    - 02_훈련데이터_테스트데이터_나누기
     - 샘플링편향 최소화 파라미터 : stratify (sklearn model_selection tran_test_split)
     - KNN 원인분석 : distances, indexes = kn.kneighbors([[25,150]]) 이웃과의 거리와 인덱스를 추출해보고 결과값의 원인에대해 분석해볼수있다
- 2day
