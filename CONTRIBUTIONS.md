# 担当とチーム成果の確認先

2026-09-14に、当時のNotebookとこの公開repoの履歴を照合して整理しました。新しい分析や、当時の作業履歴の再構成ではありません。

## Taiyo Moritaの担当

[最終NotebookのAuthors](https://github.com/t3-sketch/Music-Listening-Motivations/blob/9903da6a93ce3837e4818287f675826bece1b576/03-FinalProject.ipynb)に **Project Administration / Review / project proposal** と記載されています。[企画段階のNotebook](https://github.com/t3-sketch/Music-Listening-Motivations/blob/9903da6a93ce3837e4818287f675826bece1b576/00-ProjectProposal.ipynb)ではProject Administration / Researchと記載されており、READMEの担当は最終成果物の表記に合わせています。

| 担当 | 公開資料から確認できること |
| --- | --- |
| 進行管理 | 最終Notebookの担当記載。企画Notebookには締切・作業予定の表もあるが、各予定を実施した証拠とは区別する |
| レビュー | 最終Notebookの担当記載。個別のレビューコメントや、各修正の発案者までは公開資料から特定できない |
| 企画提案 | 最終Notebookの担当記載とチームの企画成果物。企画全体を一人で作成したという意味ではない |

## チームとして行った分析と判断

以下はいずれも5人チームの成果です。個々の分析コードをTaiyo一人の実装として扱いません。[最終Notebook](https://github.com/t3-sketch/Music-Listening-Motivations/blob/9903da6a93ce3837e4818287f675826bece1b576/03-FinalProject.ipynb)の対応する見出しから確認できます。

| 課題・判断 | 成果物の確認箇所 |
| --- | --- |
| 複数選択の動機を回答者ごとの二値列にし、動機別に検定する | **Dataset**のMethodological note、前処理、**Analysis 1: Overall Chi-square Tests of Independence** |
| 全体の関連と「成人女性・男性の違い」という仮説を区別して検証する | **Analysis 2: Stratified Chi-square Tests for Adult Female vs. Male Respondents**と、その直後のコード・出力 |
| 仮説と一致しなかった結果も含めて解釈する | **Discusison and Conclusion**（原文の見出し表記）。成人男女では4動機とも有意差を検出できなかった |

READMEでは「有意差を検出できない」を「差が存在しない」と区別し、観測データから因果関係を結論しません。集団・カテゴリ構成の異なる検定のp値だけで、年齢と性別のどちらが重要かを順位づけることもしません。

## 公開履歴から分かる範囲

[最初の公開commit](https://github.com/t3-sketch/Music-Listening-Motivations/commit/7cd89cca)に企画・中間・最終Notebookがまとめて収録され、続く2件の`Initial commit`で最終Notebook等が更新されています。この履歴から公開後の差分は追えますが、授業期間全体の分担やレビューの経緯は復元できません。commitの投稿者だけを根拠に、すべての分析をその人の担当とは判断しません。

メンバー別の担当は[READMEのクレジット](README.md#メンバーと担当)を参照してください。
