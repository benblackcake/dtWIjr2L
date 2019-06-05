# ORDERLY Python / Django Interview
Python / Django Web Developer

Hi, Ben,

感謝您

這是根據您的回覆所訂製的問題，大約會花費 3- 5 小時的挑戰時間

若您決定要開始這項挑戰，請 fork 此專案，並將每個問題的答案放至對應的資料夾

完成後，請發個PR到此專案



### 挑戰一: OO觀念運用 (folder: x_1)

> 現在您的手上有 3 支手機，手機來自不同品牌，其規格屬性大同小異，但各自擁有一項特殊功能，請使用OO繼承及如下的規格，設計出這三支手機的class。

```
手機共通屬性: price, camera_count, screen_size
特殊功能: special_freature() 

手機一 google phone:
price=10, camera_count=3, screen_size=5
special_freature 可以將輸入的 INT list 進行相乘，並回傳結果
例如: 輸入 [3,5,7] 回傳 105

手機二 taiwan phone:
price=20, camera_count=1, screen_size=3
special_freature 輸入一個數字自動回傳Fibonacci斐波那契數列的運算結果
例如: 輸入 33 回傳 3524578

手機三 apple phone:
price=30, camera_count=2, screen_size=10
special_freature 輸入2個數字自動運算 p x 取 y 
例如: 輸入(x=5, y=3)  回傳 60
```



### 挑戰二: 動態 module import 與 reload 觀念運用 (folder: x_2)

> 請設計一個 module , 它內建一個 Attr_X 屬性會在被 import 時根據當下timestamp是奇偶數來決定是 true(奇數) or false (偶數)，且一旦決定就不會更改。

> 請設計一個 for loop ，總共會執行 10 次，每次執行會隨機 sleep 1 ~ 9秒，且每次都會重新 reload 上述 module，並印出 X 的值




### 挑戰三: pip 及 Django 實作  (folder: x_3)

> 請參考 https://github.com/twtrubiks/django-tutorial 的教學，將您的Django 運行起來，並進行以下步驟:

1) 使用 pip 將你安裝的所有 python 模組及其版本變成一個 requirement 檔案
2) 將 Django 後台路徑從 /admin 修改成 /superadmin 
3) 新增一個 django app "ilovecoffee", 並於settings.py啟用它
4) 在 ilovecoffee 中，新增 models.py 檔 ，並創建一個 Coffee class, 不需要任何屬性和功能 (請注意這不代表class code裡面沒東西)
5) 在當前的虛擬環境中使用 python manage.py shell，並將 Coffee import 進來，將結果截圖放至此資料夾，取名為 coffee.jpg


## 當您挑戰結束時，請在您的最後一次 commit 中輸入您對此份工作，在程式上的期待，謝謝您。

