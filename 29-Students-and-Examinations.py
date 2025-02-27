import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_pairs = students.merge(subjects, how="cross")
    exam_counts = examinations.groupby(["student_id", "subject_name"]).size().reset_index(name="attended_exams")
    result = all_pairs.merge(exam_counts, on=["student_id", "subject_name"], how="left")
    result["attended_exams"] = result["attended_exams"].fillna(0).astype(int)
    result["student_name"] = result["student_name"].where(result["student_name"].notna(), None)
    result = result[["student_id", "student_name", "subject_name", "attended_exams"]].sort_values(by=["student_id", "subject_name"])

    return result
