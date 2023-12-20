import mysql.connector

def update_scores(db_config):
    try:
        # 连接到MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 获取表中的总记录数
        cursor.execute("SELECT COUNT(*) FROM myadmin_options")
        total_records = cursor.fetchone()[0]

        # 对于每条记录，更新score字段
        for i in range(1, total_records + 1):
            score = (i - 1) % 5 + 1  # 计算score值（1, 2, 3, 4, 5循环）
            cursor.execute("""
                UPDATE myadmin_options
                SET score = %s
                WHERE id = %s
            """, (score, i))
        
        # 提交事务
        conn.commit()
        print("Score更新成功")

    except mysql.connector.Error as err:
        print("发生错误:", err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'psychology'
}

# 调用函数
update_scores(db_config)
