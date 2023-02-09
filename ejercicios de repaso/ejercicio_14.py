if __name__ == "__main__":
    def media(valores):
        sum = 0
        for n in valores:
            sum += n
        return sum/len(valores)
    print(int(media([8, 6, 0, 9, 4, 5, 1, 2])))
