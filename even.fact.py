{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQeqYDAqw+plBCJZ2nWi+8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kartikthakur99/Davis_Training/blob/main/even.fact.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z3A7YiiXQniG"
      },
      "outputs": [],
      "source": [
        "num = int(input(\"Enter a number: \"))\n",
        "\n",
        "print(\"Even factors of\", num, \"are:\")\n",
        "\n",
        "for i in range(1, num + 1):\n",
        "    if num % i == 0 and i % 2 == 0:\n",
        "        print(i)"
      ]
    }
  ]
}