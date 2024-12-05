# [Gold II] 1의 개수 세기 - 9527 

[문제 링크](https://www.acmicpc.net/problem/9527) 

### 성능 요약

메모리: 2020 KB, 시간: 0 ms

### 분류

비트마스킹, 수학, 누적 합

### 제출 일자

2024년 12월 5일 13:34:41

### 문제 설명

<p>두 자연수 A, B가 주어졌을 때, A ≤ x ≤ B를 만족하는 모든 x에 대해 x를 이진수로 표현했을 때 1의 개수의 합을 구하는 프로그램을 작성하시오.</p>

<p>즉, f(x) = x를 이진수로 표현 했을 때 1의 개수라고 정의하고, 아래 식의 결과를 구하자.</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 111.4%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-munderover><mjx-over style="padding-bottom: 0.2em; padding-left: 0.474em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D435 TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base style="padding-left: 0.02em;"><mjx-mo class="mjx-lop"><mjx-c class="mjx-c2211 TEX-S2"></mjx-c></mjx-mo></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-texatom space="2" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D453 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><munderover><mo data-mjx-texclass="OP">∑</mo><mrow data-mjx-texclass="ORD"><mi>x</mi><mo>=</mo><mi>A</mi></mrow><mrow data-mjx-texclass="ORD"><mi>B</mi></mrow></munderover><mrow data-mjx-texclass="ORD"><mi>f</mi><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[\sum_{x=A}^{B}{f(x)}\]</span> </mjx-container></p>

### 입력 

 <p>첫 줄에 두 자연수 A, B가 주어진다. (1 ≤ A ≤ B ≤ 10<sup>16</sup>)</p>

### 출력 

 <p>1의 개수를 세어 출력한다.</p>

