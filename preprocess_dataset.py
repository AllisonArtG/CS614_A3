import pandas as pd


def preprocess_dataset(file_path, new_file_path):
    df = pd.read_csv(file_path)

    df.rename(columns={'clean_comment': 'comment', 'category': 'label'}, inplace=True)

    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    df['label'] = df['label'].replace(0, "neutral")
    df['label'] = df['label'].replace(-1, 0) #negative
    
    df = df[df.label != "neutral"]

    df.to_csv(new_file_path, index=False)


if __name__ == "__main__":
    preprocess_dataset("Reddit_Data.csv", "Reddit_Data_New.csv")
