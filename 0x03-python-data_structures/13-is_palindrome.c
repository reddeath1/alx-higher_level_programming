#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
  * is_palindrome - Main a function that check if a list is a palindrome.
  * @head: A pointer to the head of the list.
  * Return: always.
  */
int is_palindrome(listint_t **head)
{
	listint_t *tmpo = *head;
	int nodes = 0, i = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (tmpo)
	{
		nodes++;
		tmpo = tmpo->next;
	}
	array = malloc(sizeof(int) * nodes);
	tmpo = *head;
	while (tmpo)
	{
		array[i++] = tmpo->n;
		tmpo = tmpo->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (array[i] != array[nodes - 1 - i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
