# Tool
업무 자동화 tool 정리

## Markdown 관련
- conv_formula.py: markdown 수식 변환 모듈
    - 실행방법: python conv_formula.py [마크다운 경로]
    - 예시: ```python conv_formula.py '/hsyang/seminar/rl/test.md'```
    - 구현 모습
      - before: ```$R_t = X_t + Y_t$``` 
      - after: ```$`R_t = X_t + Y_t`$``` <br><br>    
- conv_img_form.py: markdown 이미지 form 변환 모듈
    - 실행방법: python conv_img_form.py --path=[마크다운 경로] --width=[너비] --height=[높이]
    - 예시: ```python conv_img_form.py --path=/hsyang/seminar/rl/test.md --width=50% --height=50%```
    - 구현 모습
      - before: ```![](/test/image.png)``` 
      - after: ```<img src="/test/image.png" width="50%" height="50%">```<br><br>
- conv_md.py: markdown 수식 변환 + 이미지 form 변환 모듈
    - 실행방법: python conv_md.py --path=[마크다운 경로] --width=[너비] --height=[높이]
    - 예시: ```python conv_md.py --path=/hsyang/seminar/rl/test.md --<br><br>