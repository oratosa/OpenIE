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

* テキストファイルの分割  
  * 月単位のメールが1ファイルにまとまっているため分割する  
    csplit -k -f 2020-July- 2020-July.txt '/^From /' '{9999}'


* ヘッダー処理  
  * email.parserのParserに任せる  
    From:, Date:, Subject:, In-Reply-To:, References:, Message-ID:

  * 追加処理  
    * From
      メールアドレス(送信者名)になっているが，とりあえずまとめたままにしておく
      分割が必要になってから処理を検討する
    * References
      複数のMessage-IDが含まれていたり，改行がある場合がある  
      -> 複数のMessage-IDを1セルにまとめておくことにする

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

* Sentenceの処理
  * 1文のトークン数が多すぎる文は取り込まない
  * 1文内にインライン表記の>>が含まれている文は取り込まない
  * ほぼ同じ文は統合する

* フッターの除去
  * てきとうなパターンが思いつかないので保留
