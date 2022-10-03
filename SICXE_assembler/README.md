# SIC/XE Version2

## 使用說明
- 執行方式: 開啟命令提示字元到該層資料夾，輸入python assembler.py 檔案名.asm 即可輸出該 assembly 組譯出的machine code。
  > 範例:
  > python assembler.py textbooksicxe.asm

## 檔案介紹
- 主要執行的檔案有
  1. assembler.py: 
    > 為主程式
  2. sic.py: 
    > 紀錄sic/xe的指令與對應的opcode和相應的instruction format
  3. sicasmparser.py
    > 將讀進來的.asm檔案，拆成三個部分: (label, opcode, oprand)
  4. objfile.py
    > 將準備好要寫入.obj的文字準備好後，並存入.obj
  
  :alien:備註: 測試的.asm檔案放在"asm_Language_for_testing"資料夾內:alien:
