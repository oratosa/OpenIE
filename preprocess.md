* メールのヘッダー例  
  From ziningy1 at andrew.cmu.edu  Wed Jul  1 21:49:35 2020  
  From: ziningy1 at andrew.cmu.edu (Ethan Ye)  
  Date: Wed, 1 Jul 2020 17:49:35 -0400  
  Subject: [Wiki-research-l] Wikipedia ORES Research Study Looking for  
	Participants  
  In-Reply-To: <CACP3XfoFBFyM1Ft1EMeiceaQhOMR_62ytHn_pbdDtd02v9wedQ@mail.gmail.com>  
  References: <CAE4fJj8bAoCLbs56g8fMo5Ek7GFk1h15ZhSJ7wy3h_KxLxhmTw@mail.gmail.com>  
   <CACP3XfoFBFyM1Ft1EMeiceaQhOMR_62ytHn_pbdDtd02v9wedQ@mail.gmail.com>  
  Message-ID: <CAE4fJj-un1Um+3aE1jTe9b8WQZuFLMaaFmCJ9zNtzTkuUja0Rw@mail.gmail.com>  

* 識別方法
  * Starting point  
    From .+ at .+ \d{4}
  * From  
    From: .+ at .+ (.+)  
    sender mail addressとsender nameに分割する
  * Date  
    Date: .+
  * Subject  
    Subject: .+  
    改行がある場合があるので対応する  
  * In-Reply-To:
  * References:  
    改行がある場合がある
  * Message-ID:

* スキーマ
  * スレッド  
    Message-ID, In-Reply-To, Referencesの属性を持つテーブル
  * メール  
    Messega-ID, From, Date, Subject, Bodyの属性を持つテーブル

* Bodyの処理  
  * インラインの開始の文字列はセンテンスとして取り込まない  
    [(On)\w*,\w*,(\d{4})\w*(<.*>).(wrote:)]  
    On Tue, Jun 30, 2020 at 3:01 PM Netha Hussain <nethahussain at gmail.com> wrote:  
  * インラインの本文はセンテンスとして取り込まない  
    ^(>>|>)

* フッターの除去
  * てきとうなパターンが思いつかないので保留
