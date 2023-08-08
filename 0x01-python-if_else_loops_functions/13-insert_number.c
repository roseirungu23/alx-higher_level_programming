#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly-linked list
 * @head: a pointer to the head of linked list
 * @number: number to insert
 * Return: Null if it fails or a pointer to the new node if otherwise
 */
listint_t *insert_node(listint_t **head, int number);
{
	listint *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
