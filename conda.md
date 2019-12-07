# conda 설치 리스트 출력
conda list

# conda 가상환경 리스트 출력(현재 활성화된 가상환경 앞에는 *가 붙음)
conda env list

# conda 새로운 가상환경 만드는 방법
conda create -n ENV_NAME python=3.7.3

# conda 가상환경 삭제
conda env remove -n ENV_NAME

# conda 가상환경 활성화(윈도우에선 앞에 source 붙여야함)
source activate ENV_NAME

# conda 가상환경 비활성화
conda deactivate

# 주피터노트북 conda env 추가
python -m ipykernel install --user --name [virtualEnv] --display-name "[displayKenrelName]"