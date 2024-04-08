import pandas as pd

# 1열 6행의 데이터프레임 생성
data = {'Column1': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)

# 행과 열을 바꾸기 (Transpose)
df_transposed = df.T

print("원본 데이터프레임:")
print(df)

print("\n변경된 데이터프레임:")
print(df_transposed)