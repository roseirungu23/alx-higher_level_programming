#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *man = list;
	listint_t *woman = list;

	if (!list)
		return (0);

	while (man && woman && woman->next)
	{
		man = man->next;
		woman = woman->next->next;
		if (man == woman)
			return (1);
	}

	return (0);
}
