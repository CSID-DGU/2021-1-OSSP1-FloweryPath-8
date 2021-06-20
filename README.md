OSR을 적용한 문장 분류 시스템   
============================   
# 2021-1-OSSP1-FloweryPath-8
팀원: 김규열 유천일 조건형 조성운 진하빈 최용진   

꽃길팀
------
* 혐오성 문장, 일베 문장, 성차별 문장과 Unknown 문장으로 4가지 클래스 문장 분류   
* k-fold 교차 검증 적용   
* Unknown 처리를 위한 OpenMax 구현   
Requirement   
-----------   
* tensorflow   
* keras   
* Tokenizer   
구현 환경 및 언어   
-----------------
환경: Jupyter Notebook   
언어: Python   


실행 결과
---------
#### Unknown 문장   
입력 :   
![image](https://user-images.githubusercontent.com/80958412/122686262-203a3d80-d24b-11eb-9ca5-d05c319f80de.png)   
출력 :   
![image](https://user-images.githubusercontent.com/80958412/122686324-54156300-d24b-11eb-8fec-db6238875637.png)   

#### 혐오성 문장
입력 :   
![image](https://user-images.githubusercontent.com/80958412/122686363-81faa780-d24b-11eb-9f84-b15b4fa866ec.png)   
출력 :   
![image](https://user-images.githubusercontent.com/80958412/122686368-8fb02d00-d24b-11eb-9d7e-a79f010d8400.png)   
