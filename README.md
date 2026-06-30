# 🎧 音楽を聴く動機は、年齢・性別で決まるのか？

### Are music-listening motivations associated with age and gender? — A Chi-square study

**COGS 108 (Data Science in Practice) Final Project — UC San Diego**

---

## 概要

「リラックスのため」「気分を上げるため」といった音楽を聴く動機が、聴き手の**年齢層・性別**と統計的に関連するのかを検証したデータ分析プロジェクト。Spotifyユーザー調査データ（27,543件）に対し、**カイ二乗独立性検定**を用いて4つの聴取動機それぞれとデモグラフィック属性の関連を分析した。結論として、**年齢は一部の動機（リラックス／気分高揚）と有意に関連する一方、成人男女間では動機に有意差が見られない**ことを明らかにした。

## リサーチクエスチョン

> 個人のデモグラフィック属性（年齢層・性別）と、音楽を聴く主な動機（リラックス、社交、悲しみ等）の間に、統計的に有意な関連はあるか？

年齢・性別を独立変数、聴取動機を従属変数とし、すべてカテゴリ変数であることからピアソンのカイ二乗独立性検定を採用した。

## 主な発見

**年齢 × 動機**（全データ）

| 聴取動機 | χ² | p値 | 有意 |
| --- | ---: | ---: | :---: |
| Relaxation and stress relief | 35.94 | < 0.001 | ✅ |
| Uplifting and motivational | 271.90 | < 0.001 | ✅ |
| Sadness or melancholy | 1.25 | 0.535 | ❌ |
| Social gatherings or parties | 4.85 | 0.0885 | ❌ |

→ **Young Adults（20〜35歳）** がリラックス（約41%）・気分高揚（約18%）の動機を他世代より高い割合で選択。社会人になるストレスが、自己調整目的の音楽聴取を押し上げている可能性を示唆。

**性別 × 動機（成人男女のみ・20歳以上）**

層別すると、4動機すべてで有意差なし（p = 0.49〜0.84）。リラックスは女性40.1% vs 男性39.9%（差0.2pt、p = 0.8361）。

→ 全データの性別検定では全動機が有意に見えたが、それは「Others」カテゴリが動機プロファイルを大きく異にしていたことによる**見かけの有意性**であり、成人男女に絞ると関連は消失した。Edison Research(2025)由来の「成人女性はリラックス動機が高い」という仮説は**支持されなかった**。

**総括**: このデータにおける最も強いデモグラフィック信号は**性別ではなく年齢**。仮説は部分的に支持された。

## 分析手法と工夫した点

- **6〜12歳の除外**: Spotifyの利用規約（13歳以上）を踏まえ、家族アカウント共有によるノイズの可能性が高いこの層を分析から除外（28,546 → 27,543件）。
- **explode ではなく One-Hot Encoding**: 動機列は複数選択（カンマ区切り）だったため、`explode` で行を展開すると同一回答者が重複し、カイ二乗検定が前提とする**観測の独立性が崩れる**。これを回避するため4つの動機を二値列に One-Hot 化し、動機ごとに独立した検定を実施した。
- **動機ごとの個別検定**: 単一の 3×4 分割表ではなく、動機×デモグラフィックで個別にカイ二乗検定を行い、どの動機が年齢／性別依存かを切り分けた。
- **層別分析による交絡の特定**: 全体検定の有意性が「Others」カテゴリと思春期層の混入に由来することを、成人男女への層別で突き止めた。広い分析と狭い分析が異なる結論を示す理由を明示。
- **クラスバランス確認**: カイ二乗の期待度数 ≥ 5 を満たすか、Age×Gender のクロス集計でスパースセルの有無を事前検証。

## ディレクトリ構成

```
.
├── 00-ProjectProposal.ipynb       # プロジェクト提案
├── 01-DataCheckpoint.ipynb        # データチェックポイント
├── 02-EDACheckpoint.ipynb         # 探索的データ分析
├── 03-FinalProject.ipynb          # 最終分析（メイン）
├── data/
│   ├── 00-raw/                    # 生データ（Spotify調査xlsx）
│   ├── 01-interim/
│   └── 02-processed/              # 前処理済みデータ
├── modules/
│   ├── analysis.py                # 集計サマリ等のヘルパー
│   └── get_data.py
└── results/
```

## 実行方法

```bash
# 1. 依存ライブラリのインストール
pip install pandas numpy matplotlib seaborn scipy openpyxl jupyter

# 2. Jupyter を起動し、03-FinalProject.ipynb を上から実行
jupyter notebook
```

データセットは Kaggle の [Spotify User Behavior Survey Data](https://www.kaggle.com/datasets/coulsonlll/spotify-user-behavior-survey-data) を使用。

## 使用技術

| カテゴリ | 技術 |
| --- | --- |
| 言語 | Python（Jupyter Notebook） |
| データ処理 | pandas / numpy |
| 可視化 | matplotlib / seaborn |
| 統計検定 | scipy（`chi2_contingency`） |
| データI/O | openpyxl |

## データセット

- **出典**: Spotify User Behavior Survey Data（Kaggle、無料利用可）
- **件数**: 生データ 28,546件 → クリーニング後 27,543件
- **使用変数**: `Age`（3層に統合）、`Gender`（Female / Male / Others）、`music_Influencial_mood`（4動機に One-Hot 化）

## 限界と今後

- **サンプリングバイアス**: Spotifyユーザー、特に若年層に偏っており（Young Adults が約39%）、一般集団を代表しない可能性。
- **自己申告データ**: 主観的回答に基づくため、想起バイアス・社会的望ましさバイアスを含みうる。
- **横断データ**: 一時点の観測であり、個人の動機が加齢でどう変化するかは追えない。発達的変化とコホート効果を区別するには縦断データが必要。
- **今後**: 縦断研究、年齢ビンの均等化、「Others」カテゴリの個別分析、他プラットフォームでの再現。

## メンバーと担当

本プロジェクトは COGS 108 のグループ課題（5名）として実施。

| メンバー | 担当 |
| --- | --- |
| **Taiyo Morita** | Project Administration / Review / Project Proposal |
| Christina Lin | Data / Revision / Project Proposal |
| Amberly Truong | Data / Writing / Project Proposal |
| Rohan Chidurala | Data / Revision |
| Shazi Bidarian | Data / Revision |
