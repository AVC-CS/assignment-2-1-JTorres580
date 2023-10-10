def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    print("Welcome to the Male/Female Percentage Ratio!\n")
    num_males = int(input("Enter the number of males in the classroom: "))
    num_females = int(input("Enter the number of females in the classroom: "))

    total_students = num_males + num_females

    m_perc = (num_males / total_students) * 100
    f_perc = (num_females / total_students) * 100   

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    print(f"\nPercentage of males in the classroom: {m_perc:.2f}%")
    print(f"Percentage of females in the classroom: {f_perc:.2f}%")
    print(f"\nClassroom Total: {total_students} Students")

    return m_perc, f_perc


if __name__ == '__main__':
    main()
