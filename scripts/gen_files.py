'''
python3 -m scripts.gen_files > cvt.log 2>&1
'''
import pandas as pd
from typing import List

from .templates import README_TEMPLATE, MARKDOWN_TEMPLATE


def flatten_excel_to_talks_by_episode(excel_path: str, sheet_name: str):
    df: pd.core.frame.DataFrame = pd.read_excel(excel_path, sheet_name=sheet_name)
    df.ffill(inplace=True)
    print(df.head())  # 查看前几行

    all_keys = df.columns.tolist()
    # shared_keys = ['期号', '标题', '北京时间', '内容', '主持人']
    shared_keys = ['期号', '标题', '北京时间', '主持人']
    diff_keys = list( set(all_keys) - set(shared_keys) )
    result_series = df.groupby(shared_keys)\
        .apply(lambda x: x[diff_keys].to_dict('records'))\
        .reset_index(name='details')

    talks_by_episode = result_series.to_dict('records')
    return talks_by_episode



def convert_talk_by_episode_to_markdown(talk_by_episode: dict):
    episode_idx = talk_by_episode['期号']
    talk_topic = talk_by_episode['标题']
    episode_time = talk_by_episode['北京时间']
    # if episode_idx == 3:
    #     raise RuntimeError( list(set([item['内容'] for item in talk_by_episode['details']])) )
    # # talk_briefs = talk_by_episode['内容']

    talk_briefs = '\n\n'.join(list(set([item['内容'] for item in talk_by_episode['details']])))
    content = MARKDOWN_TEMPLATE.format(
        episode_idx=episode_idx,
        talk_topic=talk_topic,
        episode_time=episode_time,
        talk_briefs=talk_briefs,
        # talk_briefs='',
    )
    return content


def write_content_to_file(content: str, write_path=str):
    with open(write_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"成功创建文件: {write_path}")


def create_readme_content(talks_by_episode: List[dict]):
    # | NICE 41期 | 2024.12.28 | [大模型评估的新视角：理论指标创新与下游任务应用](./files/nice_41.md) | [魏来（上交博士生）](https://waltonfuture.github.ioLLM)，[周宇轩（清华博士生）](https://zhouyx17.github.io) | 大模型评估 | [Link](./files/nice_41.md) |
    RECORD_TEMPLATE = "| NICE {episode_idx}期 | {episode_time} | [{talk_topic}](./files/nice_{episode_idx}.md) | {presenters} | {keywords} | [Link](./files/nice_{episode_idx}.md) |"
    def create_records_content():
        records_content = []
        for talk in talks_by_episode:
            # raise RuntimeError( 'talk', talk )
            records_content.append(
                RECORD_TEMPLATE.format(
                    episode_idx=talk['期号'],
                    episode_time=talk['北京时间'],
                    talk_topic=talk['标题'],
                    presenters=', '.join([item['嘉宾'] for item in talk['details']]),
                    keywords='',
            ))
        # end for
        return '\n'.join(records_content)

    records_content = create_records_content()
    # raise RuntimeError( 'records_content', records_content )
    readme_content = README_TEMPLATE.format(
        talk_records=records_content
    )
    return readme_content


def create_sidebar_content(talks_by_episode):
    SIDEBAR_RECORD_TEMPLATE = '* [NICE {episode_idx}期](./files/nice_{episode_idx}.md)'
    sidebar_content = []
    for talk in talks_by_episode:
        # raise RuntimeError( 'talk', talk )
        sidebar_content.append(
            SIDEBAR_RECORD_TEMPLATE.format(
                episode_idx=talk['期号'],
        ))
    # end for
    return '\n'.join(sidebar_content)


if __name__ == '__main__':
    print('start convert')
    talks_by_episode = flatten_excel_to_talks_by_episode(excel_path='./data/NICE直播信息.xlsx', sheet_name='2023&2024')
    talks_by_episode = talks_by_episode[:20]

    # write to files
    for talk in talks_by_episode:
        content = convert_talk_by_episode_to_markdown(talk)
        write_content_to_file(
            content=content,
            write_path=f"./docs/files/nice_{talk['期号']}.md"
        )
    # end for

    # write to readme
    readme_content = create_readme_content(talks_by_episode)
    write_content_to_file(
        readme_content,
        write_path=f"./docs/README.md"
    )

    # write to sidebar
    sidebar_content = create_sidebar_content(talks_by_episode)
    # raise RuntimeError('sidebar_content', sidebar_content)
    write_content_to_file(
        sidebar_content,
        write_path=f"./docs/_sidebar.md"
    )
