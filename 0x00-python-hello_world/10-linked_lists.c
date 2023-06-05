#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - main function that prints all elements of a listint_t list
 * @h: The pointer to head of list
 * Return: (The number of nodes)
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *c;
	unsigned int n;

	c = h;
	n = 0;
	while (c != NULL)
	{
		printf("%i\n", c->n);
		c = c->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - function to add a new node at the beginning of a listint_t list
 * @head: The pointer to a pointer of the start of the list
 * @n: The integer to be included in node
 * Return: (The address of the new element or NULL)
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = n;
	node->next = *head;
	*head = node;

	return (node);
}

/**
 * free_listint - main function to frees a listint_t list
 * @head: pointer to list to be freed list
 * Return: (void)
 */
void free_listint(listint_t *head)
{
	listint_t *c;

	while (head != NULL)
	{
		c = head;
		head = head->next;
		free(c);
	}
}
