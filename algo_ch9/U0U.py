import pandas as pd
import numpy as np

def split_datas(input_file, output_file):
    # 엑셀 파일 읽기
    df = pd.read_excel(input_file, header=None)
    imp_col = { 5 : 4, 7 : 6, 'd' : 8, 'f' : 10}
    
    new_df = pd.DataFrame()
    
    # 임피던스 값 중복 검사를 위한 변수
    Rzmag_b = 0.0
    Rzphz_b = 0.0
    
    for i in range(df.shape[0]) :
        # 샘플링 데이터 처리
        temp_df = pd.DataFrame()
        for j in range(4) :
            temp_df = pd.concat([temp_df, df.iloc[i, j*24 : (j+1)*24].transpose().reset_index(drop=True)], axis=1)
        # ADC 이외 데이터 분할
        sub_cols = df.iloc[i,96:].values.reshape(1,-1)
        
        # j값, 채널, 임피던스 추출
        j, channel, Rzmag, Rzphz = sub_cols[0][1], sub_cols[0][2], sub_cols[0][4], sub_cols[0][5]
        
        # 12열로 확장
        for k in range(8) : temp_df['new_col'+str(k)] = np.nan
        temp_df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        
        temp_df.iloc[0,4:] = np.nan
        
        if Rzmag_b != Rzmag or Rzphz_b != Rzphz :
            temp_df.iloc[j * 6, imp_col.get(channel):imp_col.get(channel)+2] = [Rzmag, Rzphz]
            Rzmag_b, Rzphz_b = Rzmag, Rzphz
        
        new_df = pd.concat([new_df, temp_df]) #전체 데이터 프레임에 연결
    #출력 확인
    return new_df

def remove_noise(data_frame) :
    
    for i in range(4) :
        for j in range(data_frame.shape[0]) :
            if not pd.isna(data_frame.iloc[j,5 + (i*2)])  :
                r_s = j - 8 if j >= 8  else j
                r_e = j + 21 if data_frame.shape[0] - j > 21 else data_frame.shape[0] - j
                data_frame.iloc[r_s:r_e+1, i] = 120

    return data_frame

if __name__ == "__main__":
    # 입력 엑셀 파일명과 출력 파일명 설정
    input_excel_file = r"D:\Python_Excercise\algorithms\algo_ch9\real_testcase.xlsx"
    output_excel_file = r"D:\Python_Excercise\algorithms\algo_ch9\opt11.xlsx"

    # 함수 호출
    remove_noise(split_datas(input_excel_file, output_excel_file).reset_index(drop=True)).to_excel(output_excel_file, index=False, header=False)