#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

listint_t *_create(int n);

/**
 * insert_node -Main function that inserts a node
 * sorted in a linked list of ints
 * @head: double pointer to head of Linked List, needed for modification
 * @n: the data for new node
 * Return:(the pointer to newly created node, NULL on failure)
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *current = NULL, *new = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new = _create(n);
		*head = new;
		return (new);
	}
	current = *head;
	while (current)
	{
		/* need to insert at head */
		if (current->n >= n)
		{
			new = _create(n);
			new->next = current;
			*head = new;
			return (new);
		}
		else if (current->n <= n)
		{
			if (!current->next || current->next->n >= n)
			{
				new = _create(n);
				new->next = current->next;
				current->next = new;
				return (current->next);
			}
		}
		current = current->next;
	}
	return (NULL);
}


/**
 * _create - main function that creates a new node for the list
 * @n: the data to insert into new node
 * Return: (the pointer to newly allocated node)
 */
listint_t *_create(int n)
{
	listint_t *r = NULL;

	r = malloc(sizeof(listint_t));
	if (!r)
		return (NULL);
	r->next = NULL;
	r->n = n;
	return (r);
}
