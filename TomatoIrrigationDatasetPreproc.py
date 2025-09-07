import pandas as pd
def clean_and_preprocess_data(input_filepath, output_filepath):
    df = pd.read_csv(input_filepath)
    original_cols = df.columns
    new_cols = []
    for col in original_cols:
        new_col = col.replace(' [_ C]', '').replace(' [%]', '').replace(' [mg/kg]', '').replace(' ', '_')
        new_cols.append(new_col)
    df.columns = new_cols
    df = pd.get_dummies(df, columns=['Crop_Coefficient_stage'], prefix='Stage')
    df.to_csv(output_filepath, index=False)
    print(f"Cleaned data saved to {output_filepath}")
if __name__ == '__main__':
    input_file = 'tomato_irrigation_dataset.csv.csv'
    output_file = 'cleaned_tomato_irrigation_dataset.csv'
    clean_and_preprocess_data(input_file, output_file)