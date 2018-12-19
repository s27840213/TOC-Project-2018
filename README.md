# TOC Project 2018

## FSM
![](https://i.imgur.com/fzHOGW0.png)

## 簡介
* 這是一個系排相關的Chatbot哦!可以向他詢問關於系排的問題呦。
* 程式並無用到資料庫，而是用python中的dictionary去實作的，目前只有data中只有系排大三成員+醜男林允文哦!

## 各State功能簡介
* 簡單說各state的功能，詳細運作請看**運作流程**!
### Init State
* 無功能，只是FSM的起點和各State的返回目的地
* 隨便打個訊息就會跑去user state

### User State
* 用來選擇功能的state
	* 功能:
		* 球員訊息
		* 系排戰績
		* 系排梗圖(醜照)
### askMemb State
* 詢問球員訊息的State

### showMemb State
* 顯示球員訊息的State
### askRecord State
* 顯示系排戰績的State
### funPhoto State
* 用來傳送梗圖的State



## 運作流程

### First Step: 
* 一開始的時候再init state，當你隨便傳送一次訊息時，會進入到user state，而chatbot會傳送一段提示訊息給你哦!  
 ![](https://i.imgur.com/qPqik0X.png)

### Second Step:
* 當進入到user state，就可以開始問問題瞜!
	---
	* 輸入包含**成員、球員**的訊息時，會進入到 askMemb state，可以向chatbot詢問系排的成員哦!(ex: 我想問成員、球員啦)
		 ![](https://i.imgur.com/i5xBxmX.png)

		* 當你再次輸入一段訊息時，會進入到showMemb state，若是程式中有紀錄這個成員，chatbot會將該成員的資訊告訴你哦!
		![](https://i.imgur.com/3IkOIWq.png)
		* 若程式中沒記錄這個成員，chatbot會告知你沒有這個成員哦!
		![](https://i.imgur.com/gehpVjM.png)
		* 結束後，你可以繼續問你下一個想問的球員，若是傳送包含**沒有、no、不用、其他問題**的訊息時，則會跳回到init state
		![](https://i.imgur.com/0WONn3y.png)

	
	---
	* 輸入包含**戰績**的訊息時，會進入到 askRecord state，chatbot會跟你說系排近年來的戰績哦!(ex: 我想戰績、戰績)
	
	* ![](https://i.imgur.com/FqIn5wa.png)
		* chatbot回覆完之後會回到init state
	---
	* 輸入包含**梗圖、醜照**的訊息時，會進入到 funPhoto state，chatbot會隨機挑三張系排的圖片傳給你哦!(ex: 我想要看梗圖、我想要醜照、醜照、梗圖)
		![](https://i.imgur.com/4qKXwkh.png)

		* chatbot回覆完之後會回到init state





