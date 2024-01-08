

def sequence_alignment(seq1, seq2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
    m = len(seq1)
    n = len(seq2)

    # 初始化得分矩阵和回溯矩阵
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    traceback_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    max_score = 0
    max_i = 0
    max_j = 0

    # 填充得分矩阵和回溯矩阵
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
            delete = score_matrix[i-1][j] + gap_penalty
            insert = score_matrix[i][j-1] + gap_penalty

            # 更新得分矩阵和回溯矩阵
            score_matrix[i][j] = max(0, match, delete, insert)
            if score_matrix[i][j] == 0:
                traceback_matrix[i][j] = 0
            elif score_matrix[i][j] == match:
                traceback_matrix[i][j] = 1
            elif score_matrix[i][j] == delete:
                traceback_matrix[i][j] = 2
            elif score_matrix[i][j] == insert:
                traceback_matrix[i][j] = 3

            # 更新最大得分和对应的位置
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i = i
                max_j = j

    # 回溯，构建比对结果
    alignment_seq1 = ""
    alignment_seq2 = ""

    i = max_i
    j = max_j

    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if traceback_matrix[i][j] == 1:
            alignment_seq1 = seq1[i-1] + alignment_seq1
            alignment_seq2 = seq2[j-1] + alignment_seq2
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 2:
            alignment_seq1 = seq1[i-1] + alignment_seq1
            alignment_seq2 = '-' + alignment_seq2
            i -= 1
        elif traceback_matrix[i][j] == 3:
            alignment_seq1 = '-' + alignment_seq1
            alignment_seq2 = seq2[j-1] + alignment_seq2
            j -= 1

    return alignment_seq1, alignment_seq2, max_score

'''
# 示例用法
seq1 = "ACGTAG"
seq2 = "ACGTCAG"
alignment1, alignment2, score = sequence_alignment(seq1, seq2)

print("Sequence 1:", alignment1)
print("Sequence 2:", alignment2)
print("Alignment Score:", score)
'''

def blast(query_sequence, database):
    results = []
    threshold = 0 #需要根据实际情况进行修改
    # 遍历数据库中的每个序列
    for db_sequence in database:
        # 执行序列比对
        alignment_seq1, alignment_seq2, score = sequence_alignment(query_sequence, db_sequence)

        # 判断是否有足够高的相似性得分
        if score > threshold:
            # 将结果添加到列表中
            result = {
                "query_sequence": query_sequence,
                "database_sequence": db_sequence,
                "alignment_seq1": alignment_seq1,
                "alignment_seq2": alignment_seq2,
                "score": score
            }
            results.append(result)

    return results

# 示例用法
query_sequence = "HHTTHHS"
database = ["HTSSHS", "TTTHHS", "THSS"]  # 假设这是你的数据库

blast_results = blast(query_sequence, database)

# 打印结果
for result in blast_results:
    print("Query Sequence:", result["query_sequence"])
    print("Database Sequence:", result["database_sequence"])
    print("Alignment 1:", result["alignment_seq1"])
    print("Alignment 2:", result["alignment_seq2"])
    print("Score:", result["score"])
    print("--------")
